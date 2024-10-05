import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)

from number_utils import *
import numpy as np
from itertools import combinations
from math import log
from collections import defaultdict

'''
From the formula :math:`\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)` we get that :math:`\frac{n}{\phi(n)} = \left(\prod_{p \mid n} \left(1 - \frac{1}{p} \right) \right)^{-1}`.

This is minimal when the product :math:\prod_{p \mid n} \left(1 - \frac{1}{p}\right)` is maximal.

We notice also that if :math:`n` is prime, we have :math:`\phi(n) = n-1`, which cannot be a permutation of :math:`n`, and that if :math:`\prod_{p \mid n} \left(1 - \frac{1}{p} \right) < 1/10`, then the number of digits in :math:`\phi(n)` is smaller than the number of digits in :math:`n`, so the numbers cannot be permutations of each other.
'''

def is_permutation(nums : [int, int]) -> bool:
    nums = [list(str(nums[0])), list(str(nums[1]))]
    counts = defaultdict(int)
    for x,y in zip(*nums):
        counts[x] += 1
        counts[y] -= 1
    return not any(counts.values())

def prime_factors(num : int):
    """
    Generates the prime factors of a positive integer num that is not divisible by 2,3,5,7.
    """
    j = 11
    while(num > 1):
        for i in range(j, int(sqrt(num+0.05)) + 1):
            if(num % i == 0):
                num //= i
                j = i
                yield i
                break
        else:
            if(num > 1):
                yield num
                break

def totient(num : int, prime_factors : list[int]) -> int:
    """
    Returns the value of Euler's totient function of a number num, given its prime factors.
    """
    res = num
    for prime in prime_factors:
        res = res * (1 - 1/prime)
    return int(res)

def solution():
    max_num = 10**7 - 1
    
    # An example for a number n such that phi(n) is a permutation of n.
    result = 87109
    # The example 87109 is 11 * 7919.
    max_totient_quotient = (1 - 1/11) * (1 - 1/7919)

    # For numbers divisible by 2,3,5 or 7, we would get that n / phi(n) is smaller than max_totient_quotient.
    candidates = [num for num in range(7921, max_num + 1) if (
        num % 2 != 0
        and num % 3 != 0
        and num % 5 != 0
        and num % 7 != 0
        )]
    for num in candidates:

        print(num)

        factors = [factor for factor in prime_factors(num)]
        if(len(factors) == 1):
            continue
        totient_quotient = np.prod([(1 - 1/factor) for factor in factors])
        if(totient_quotient <= max_totient_quotient):
            continue
        if(is_permutation([num, totient(num, factors)])):
            max_totient_quotient = totient_quotient
            result = num

    return result
    

if __name__ == "__main__":
    print(solution())
