import competition_utilities as cu
import numpy as np

'''
Priors is a list of length(closed_reasons) = 5 for us.
priors[i] = fraction of 1 that a closed reason was reason[i]

the prior_benchmark predicts each sample will be closed for reason[i]
with probability priors[i] from the training set, i'e, regardless of what 
the input sample is, the output will always be the training sample averages.
'''
def main():
    priors = cu.get_priors("train.csv")
    num_samples = len(cu.get_dataframe("public_leaderboard.csv"))
    predictions = np.kron(np.ones((num_samples,1)), priors)
    cu.write_submission("prior_benchmark.csv", predictions)

if __name__=="__main__":
    main()