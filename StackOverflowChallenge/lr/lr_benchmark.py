'''
Created on Sep 6, 2012

@author: kesten
'''
from collections import Counter
import competition_utilities as cu
import features
from sklearn.ensemble import RandomForestClassifier
import numpy as np

''' Use a 1000 line file for development'''
train_file = "train_file_short.csv"
full_train_file = "train.csv"
test_file = "public_leaderboard.csv"
train_features_short_file = "train_features_short.csv"
train_y_short_file = "train_y_file.csv"
submission_file = "lr_benchmark.csv"

feature_names = [ "BodyLength"
                , "NumTags"
                , "OwnerUndeletedAnswerCountAtPostTime"
                , "ReputationAtPostCreation"
                , "TitleLength"
                , "UserAge"
                ]

def main():
    
    print("Reading the data")
    data = cu.get_dataframe(train_file)

    print("Extracting features")
    fea = features.extract_features(feature_names, data)
    print("Writing short sample features file")
    ''' preview in console '''
    print(fea.values[:4])
    print fea.describe().to_string()
    ''' save the X features data (matrix)'''
    # cu.write_submission(train_features_short_file, fea.values)
    np.savetxt(train_features_short_file, fea.values, fmt='%d', delimiter=',', newline='\n')

    
    '''train_features_short = [fea, data["OpenStatus"]]'''
    closed_reasons = data["OpenStatus"]
    closed_reasons_count = Counter(closed_reasons)

    print(closed_reasons_count.keys()[0:5])
    closed_reasons_enum = map(closed_reasons_count.keys().index, closed_reasons)    
    print(closed_reasons_enum[:9])
    
    print("Saving submission to %s" % submission_file)
    ''' save the y supervised classification data (vector) '''
    np.savetxt(train_y_short_file, closed_reasons_enum, fmt='%d', delimiter=',', newline='\n')

    '''

    Now in Octave we can do
    X=textread("train_features_short.csv", "%d", "delimiter", ",")
    y=textread("train_y_short.csv", "%d", "delimiter", ",")
    could have done this to join X and y into single file
    train_features_short = zip(fea, closed_reasons_enum)
    '''
    
if __name__=="__main__":
    main()    

        