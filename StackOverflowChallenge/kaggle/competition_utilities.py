from __future__ import division
from collections import Counter
import csv
import dateutil
import numpy as np
import os
import pandas as pd

data_path = "/home/kesten/VCP/Git/ML/StackOverflowChallenge/data"
submissions_path = "/home/kesten/VCP/Git/ML/StackOverflowChallenge/data"
if not data_path or not submissions_path:
    raise Exception("Set the data and submission paths in competition_utilities.py!")

def parse_date_maybe_null(date):
    if date:
        return dateutil.parser.parse(date)
    return None

df_converters = {"PostCreationDate": dateutil.parser.parse,
                 "OwnerCreationDate": dateutil.parser.parse}
                # "PostClosedDate": parse_date_maybe_null}

def get_reader(file_name="train-sample.csv"):
    reader = csv.reader(open(os.path.join(data_path, file_name)))
    header = reader.next()
    return reader

def get_header(file_name="train-sample.csv"):
    reader = csv.reader(open(os.path.join(data_path, file_name)))
    header = reader.next()
    return header

def get_closed_count(file_name):
    return sum(1 for q in iter_closed_questions(file_name))

def iter_closed_questions(file_name):
    df_iter = pd.read_csv(os.path.join(data_path, file_name), iterator=True, chunksize=1000)
    return (question[1] for df in df_iter for question in df[df["OpenStatus"] != "open"].iterrows())

def get_closed_indices(file_name):
    df = get_dataframe(file_name)
    return df[df["OpenStatus"] != "open"].index
    
def iter_open_questions(file_name):
    df_iter = pd.read_csv(os.path.join(data_path, file_name), iterator=True, chunksize=1000)
    return (question[1] for df in df_iter for question in df[df["OpenStatus"] == "open"].iterrows())

def get_open_indices(file_name):
    df = get_dataframe(file_name)
    return df[df["OpenStatus"] == "open"].index

def get_dataframe(file_name="train-sample.csv"):
    return pd.read_csv(os.path.join(data_path, file_name), converters = df_converters)

def get_priors(file_name):
    closed_reasons = [r[14] for r in get_reader(file_name)]
    closed_reason_counts = Counter(closed_reasons)
    reasons = sorted(closed_reason_counts.keys())
    total = len(closed_reasons)
    priors = [closed_reason_counts[reason]/total for reason in reasons]
    return priors


def get_lines(file_name, lines):
    count = 0
    out_lines = []
    for r in get_reader(file_name):
        out_lines.append(r) 
        count = count + 1
        if count >= lines:
            break
    return out_lines

def write_sample(file_name, header, sample):
    writer = csv.writer(open(os.path.join(data_path, file_name), "w"), lineterminator="\n")
    writer.writerow(header)
    writer.writerows(sample)

def write_sample_lines(file_name, header, sample, lines):
    writer = csv.writer(open(os.path.join(data_path, file_name), "w"), lineterminator="\n")
    writer.writerow(header)
    reader = get_reader("train-sample.csv")
    count = 0
    while count < lines:
        row = reader.next()
        count = count + 1
        writer.writerow(row)

''' Example use: 
        -extract a subset of features from in_file to a dataframe
        -find the outliers and their indices
        -use write_records so the entire record of each outlier can be inspected
         in full.  The dataframe only has a subset of features.
         '''
def write_records(in_file, out_file, indices):
    writer = csv.writer(open(os.path.join(data_path, out_file), "w"), lineterminator="\n")
    writer.writerow(get_header(in_file))
    reader = get_reader(in_file)
    max_ix = sorted(indices)[len(indices)-1]
    count = 0
    while count <= max_ix:
        row = reader.next()
        count = count + 1
        if count in indices:
            writer.writerow(row)

def get_records(in_file, indices):
    df = get_dataframe(file_name=in_file)
    return df.take(indices)
    
def update_prior(old_prior,  old_posterior, new_prior):
    evidence_ratio = (old_prior*(1-old_posterior)) / (old_posterior*(1-old_prior))
    new_posterior = new_prior / (new_prior + (1-new_prior)*evidence_ratio)
    return new_posterior

def cap_and_update_priors(old_priors, old_posteriors, new_priors, epsilon):
    old_posteriors = cap_predictions(old_posteriors, epsilon)
    old_priors = np.kron(np.ones((np.size(old_posteriors, 0), 1)), old_priors)
    new_priors = np.kron(np.ones((np.size(old_posteriors, 0), 1)), new_priors)
    evidence_ratio = (old_priors*(1-old_posteriors)) / (old_posteriors*(1-old_priors))
    new_posteriors = new_priors / (new_priors + (1-new_priors)*evidence_ratio)
    new_posteriors = cap_predictions(new_posteriors, epsilon)
    return new_posteriors

def cap_predictions(probs, epsilon):
    probs[probs>1-epsilon] = 1-epsilon
    probs[probs<epsilon] = epsilon
    row_sums = probs.sum(axis=1)
    probs = probs / row_sums[:, np.newaxis]
    return probs

def write_submission(file_name, predictions):
    writer = csv.writer(open(os.path.join(submissions_path, file_name), "w"), lineterminator="\n")
    writer.writerows(predictions)


''' ********Methods to aid conversion from Python to Octave **************
* RandomForest classifier automatically converts string values to ints internally.
* For preparing the data for Octave we need to do this manually.  All the features 
* in features.py are ints except for "OpenStatus".  We need to map the vector of 
* "OpenStatus" examples to a vector of ints.  One suggestions from StackOverflow:
* 
* closed_reasons is a list of strings
* closed_reasons_count = Counter(closed_reasons)
* closed_reasons_enum = map(closed_reason_count.keys().index, closed_reasons)
* closed_reasons_enum is now the same list, but as numbers

'''
