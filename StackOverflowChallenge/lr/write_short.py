import competition_utilities as cu
import features

train_file = "train-sample.csv"
full_train_file = "train.csv"
test_file = "public_leaderboard.csv"
output_file = "train_file_short.csv"
lines = 1000

feature_names = [ "BodyLength"
                , "NumTags"
                , "OwnerUndeletedAnswerCountAtPostTime"
                , "ReputationAtPostCreation"
                , "TitleLength"
                , "UserAge"
                ]

def main():
    print("Reading the data", train_file)
    header = cu.get_header(train_file)

    records = cu.get_lines(train_file, lines)
    cu.write_sample(output_file, header, records)

if __name__=="__main__":
    main()
