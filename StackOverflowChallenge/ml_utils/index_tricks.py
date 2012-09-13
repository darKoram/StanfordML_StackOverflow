'''
Created on Sep 6, 2012

@author: kesten
'''
import numpy as np

''' takes a vector of classification values from [1,classes] integers
    returns y represented as basis vectors'''

def multiclass_vs(y, classes):
    basis = np.eye(classes)
    q = [basis[i] for i in range(0,classes-1)]
    q1 = np.array(q)
    return q1[y]
    