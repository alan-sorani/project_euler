from math import factorial
import numpy as np
from functools import cache

import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

if(__name__ == "__main__"):
    chain_lengths = {}
    large_num = 10**5
    factorizations = factorize_up_to(large_num)
    print(f"Factorized numbers up to {large_num}.")
    for i in range(1, large_num+1):
        if(i in chain_lengths.keys()):
            continue

        chain = [i]
        temp = int(np.sum(divisors[i]))

        while(temp not in chain_lengths.keys() and temp not in chain and temp <= large_num):
            chain += [temp]
            temp = int(np.sum(divisors[temp]))
        if(temp > large_num):
            for j in range(0, length(chain)+1):
                chain_lengths[chain[j]] = -float('inf')
        elif(temp in chain):
            count = 1
            first_loop_index = chain.index(temp)
            last_loop_index = len(chain) - 1
            loop_length = last_loop_index - first_loop_index + 1
            for j in range(first_loop_index,len(chain)):
                chain_lengths[chain[j]] = loop_length
            for j in range(first_loop_index-1,-1,-1):
                chain_lengths[chain[j]] = count + loop_length
                count += 1
        else:
            length = chain_lengths[temp] + 1
            for j in range(len(chain)-1,-1,-1):
                chain_lengths[chain[j]] = length
                length += 1

    first_in_longest = max(chain_lengths, key=chain_lengths.get)
    print(first_in_longest)
