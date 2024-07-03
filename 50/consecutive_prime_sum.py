import numpy as np

import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

def solution():
    max_num = 10**6
    primes = sieve_of_eratosthenes(max_num)
    max_chain_length = 0
    i = 0
    while(np.sum(primes[:i+1]) < max_num):
        i += 1
    max_chain_length = i
    
    res = 0
    for chain_length in range(max_chain_length+1, 1, -1):
        for i in range(len(primes) - chain_length + 1):
            sum_ = np.sum(primes[i : i+chain_length])
            if(sum_ < max_num and sum_ in primes):
                return sum_


if __name__ == "__main__":
    print(solution())
