# Rfunc replicates a function in R that can't be found in Python
import numpy as np

def sliceR(arr):
    col =  arr.shape[1]
    for column in range(col):
        print arr[:,column]
        
# import class problem
# function replication problem
  # needs to return every slice but the one called...
