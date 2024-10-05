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

This is minimal when the product :math:\prod_{p \mid n} \left(1 - \frac{1}{p}\right)` is maximal. Taking the logarithm of this, we have to maximize :math:`\sum_{p \mid n} \log\left(1 - \frac{1}{p}\right)`.
'''

def solution():
    primes = sieve_of_eratosthenes(10**7)

if __name__ == "__main__":
    print(solution())
