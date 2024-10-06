import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import sieve_of_eratosthenes

import numpy as np
from collections import defaultdict
from itertools import product

'''
We go over all triples of primes :math:`(a,b,c)` up to :math:`\sqrt{50000000}` and count how many numbers are of the form :math:`a^2 + b^3 + c^4` for such primes.
'''


def solution():
    large_num = 5 * 10**7
    primes_1 = sieve_of_eratosthenes(int(np.ceil(np.sqrt(large_num))))
    primes_2 = [prime for prime in primes_1 if prime**3 < large_num]
    primes_3 = [prime for prime in primes_2 if prime**4 < large_num]
    numbers_found = set()
    triples = product(primes_1, primes_2, primes_3)
    for (a,b,c) in triples:
        if(a**2 + b**3 + c**4 < large_num):
            numbers_found.add(a**2 + b**3 + c**4)

    assert(28 in numbers_found)
    assert(33 in numbers_found)
    assert(49 in numbers_found)
    assert(47 in numbers_found)
    print(len(numbers_found))

if __name__ == "__main__":
    solution()
