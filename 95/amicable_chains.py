import numpy as np
from functools import cache

import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

max_val = 10**6
primes = sieve_of_eratosthenes(max_val)

@cache
def sum_divisors(num : int, max_val : int):
    """
    Returns the sum of proper divisor of a number, or infinity if the result would be above a given maximum value.
    The parameter prime_lower_bound determines that num doesn't have prime factors below this value.
    """
    assert num >= 0, f"The function sum_divisors received the negative value {num}."
    if(num in {0,1}):
        return num
    i = 0
    res = -1
    for prime in primes:
        if(prime**2 > num):
            return num + 1
        deg = 0
        while(num % prime == 0):
            num /= prime
            deg += 1
        if(deg > 0):
            res = np.sum([prime**i for i in range(deg+1)]) * sum_divisors(num, max_val)
            break
    if(res == -1):
        raise ValueError(f"Couldn't find a divisor of {num}.")
    if(res > max_val):
        return float('inf')
    assert res > num, f"Calculated sum of divisors {res} for {num}, where the latter should be smaller."
    return res

if(__name__ == "__main__"):
    chain_lengths = {}

    for i in range(1, max_val+1):
        if(i in chain_lengths.keys()):
            continue

        chain = [i]
        temp = sum_divisors(i, max_val) - i

        while(temp not in chain_lengths.keys() and temp not in chain and temp <= max_val):
            chain += [temp]
            assert i < 2 or temp > 0, f"{chain} has a non-positive element"
            temp = sum_divisors(temp, max_val) - temp
        if((temp not in chain) or (temp > max_val)):
            for j in range(0, len(chain)):
                chain_lengths[chain[j]] = -float('inf')
        else:
            first_loop_index = chain.index(temp)
            last_loop_index = len(chain) - 1
            loop_length = last_loop_index - first_loop_index + 1
            for j in range(first_loop_index,len(chain)):
                chain_lengths[chain[j]] = loop_length
            for j in range(first_loop_index):
                chain_lengths[chain[j]] = -float('inf')
            print(chain[:first_loop_index], chain[first_loop_index:])
    
    first_in_longest = max(chain_lengths, key=chain_lengths.get)
    chain = []
    temp = first_in_longest
    while(temp not in chain):
        chain += [temp]
        temp = sum_divisors(temp, max_val) - temp
    print(chain)
