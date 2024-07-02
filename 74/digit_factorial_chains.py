from math import factorial
import numpy as np
from functools import cache

def sum_digit_factorials(num : int):
    digits = [int(digit) for digit in list(str(num))]
    return int(np.sum([factorial(digit) for digit in digits]))

if(__name__ == "__main__"):
    chain_lengths = {}
    for i in range(1, 10**6):
        if(i in chain_lengths.keys()):
            continue

        chain = [i]
        temp = sum_digit_factorials(i)

        while(temp not in chain_lengths.keys() and temp not in chain):
            chain += [temp]
            temp = sum_digit_factorials(temp)
        if(temp in chain):
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

    print(list(chain_lengths.values()).count(60))
            
