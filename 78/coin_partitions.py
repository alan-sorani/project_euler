import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from combinatorics_utils import sums_of_naturals

from math import comb
from functools import cache

'''
We use a recursion based on the Pentagonal Theorem for the partition function.
'''

def generalized_pentagonal(n : int) -> int:
    '''
    Returns the n'th generalized pentagonal number.
    '''
    if(n == 0):
        return 0
    if(n % 2 == 1):
        m = (n + 1) / 2
    else:
        m = -n / 2
    return int(m * (3 * m - 1)/2)

@cache
def partition_function(n : int) -> int:
    '''
    Returns the n'th value of the partition function.
    '''
    if(n in {0,1}):
        return 1
    i = 1
    pentagonal = 1
    res = 0
    while(pentagonal <= n):
        pentagonal = generalized_pentagonal(i)
        if(i % 4 in {1,2}):
            res += partition_function(n - pentagonal)
        else:
            res -= partition_function(n - pentagonal)
        pentagonal = generalized_pentagonal(i)
        i += 1
    return res

'''
The number of ways that n coins can be separated into k piles is the number of ways to write n as the sum of k natural numbers.
We therefore use sums_of_naturals which sums these values across all values of k, and which we used in previously-solved problems.
'''

def solution():
    n = 1
    res = 1
    while(res % 10**6 != 0):
        n += 1
        res = partition_function(n)
    return n

if __name__ == "__main__":
    print(solution())
