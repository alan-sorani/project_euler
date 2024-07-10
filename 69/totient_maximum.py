import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)

from number_utils import *
import numpy as np
from itertools import combinations
from math import log

'''
From the formula :math:`\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)` we get that :math:`\frac{n}{\phi(n)} = \left(\prod_{p \mid n} \left(1 - \frac{1}{p} \right) \right)^{-1}`.

This is maximal when the product :math:\prod_{p \mid n} \left(1 - \frac{1}{p}\right)` is minimal. Taking the logarithm of this, we have to minimize :math:`\sum_{p \mid n} \log\left(1 - \frac{1}{p}\right)`.
'''

def prime_factors(num : int, primes : list[int]):
    res = []
    for prime in primes:
        if(num % prime == 0):
            res += [prime]
            while(num % prime == 0):
                num /= prime
    return res

def log_expression(primes_factors : list[int]) -> float:
    return 0
     

def solution():
    primes = sieve_of_eratosthenes(10**6)
    i = 1
    min_prod = 2
    res = None
    while(min_prod <= 10**6):
        res = min_prod
        i += 1
        min_prod = np.prod(primes[:i])
    return res


if __name__ == "__main__":
    print(solution())
