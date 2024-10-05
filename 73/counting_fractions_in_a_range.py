import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)

from number_utils import *
from combinatorics_utils import *
import numpy as np

'''
For each value of d between 2 and 12000, we count how many positive integers in the range (d/3,d/2) are coprime to it.
'''
        
def solution():
    res = 0
    for d in range(2,12001):
        for n in range(int(np.floor(d/3))+1, int(np.ceil(d/2))):
            res += (np.gcd(d,n) == 1)
    return res
        

if __name__ == "__main__":
    print(solution())
