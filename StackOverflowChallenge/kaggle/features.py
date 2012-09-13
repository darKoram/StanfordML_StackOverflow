import competition_utilities as cu
import csv
import datetime
import numpy as np
import features
import pandas as pd
import re

strlen = lambda x: len(str(x))

def camel_to_underscores(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

##############################################################
###### FEATURE FUNCTIONS
##############################################################

def body_length(data):
    '''return data["BodyMarkdown"].apply(len)  this is wrong.  it gives the
    length of the column no matter what the length of the element'''
    return data["BodyMarkdown"].map(strlen)

def num_tags(data):
    return pd.DataFrame.from_dict({"NumTags": [sum(map(lambda x:
                    pd.isnull(x), row)) for row in (data[["Tag%d" % d
                    for d in range(1,6)]].values)] } ) ["NumTags"]

def title_length(data):
    return data["Title"].map(strlen)

'''user_age is actually number of seconds user has been registered on S.O.'''
def user_age(data):
    return pd.DataFrame.from_dict({"UserAge": (data["PostCreationDate"]
            - data["OwnerCreationDate"]).apply(lambda x: x.total_seconds())})

###########################################################

def extract_features(feature_names, data):
    fea = pd.DataFrame(index=data.index)
    for name in feature_names:
        if name in data:
            fea = fea.join(data[name])
        else:
            fea = fea.join(getattr(features, camel_to_underscores(name))(data))
    return fea

if __name__=="__main__":
    feature_names = [ "BodyLength"
                    , "NumTags"
                    , "OwnerUndeletedAnswerCountAtPostTime"
                    , "ReputationAtPostCreation"
                    , "TitleLength"
                    , "UserAge"
                    ]
              
    data = cu.get_dataframe("/home/kesten/VCP/Git/ML/StackOverflowChallenge/data/train-sample.csv")
    features = extract_features(feature_names, data)
    print(features)

    