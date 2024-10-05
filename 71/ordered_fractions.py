import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)

from number_utils import *
import numpy as np

'''
For each value d for the denominator, the only option for n/d to be the closest reduced proper fraction to the left of 3/7 is if n/d is the closest proper fraction to the left of 3/7. Otherwise, n/d has a reduced form n'/d' with denominator d' <= 10**6 that is closer to 3/7 from the left.

So, for each possible value of d, we consider the highest value n/d the is less than 3/7, and look at the numerator of its reduced form.
'''

def gcd(a : int, b : int) -> int:
    if(b == 0):
        return a
    return gcd(b, a % b)

def solution():
    closest_fraction = 0
    res = 0
    for d in range(10**6, 1, -1):
        n = int(d * 3/7)
        if(d % 7 == 0):
            n -= 1
        if(n/d > closest_fraction):
            closest_fraction = n/d
            res = n / gcd(n,d)
    return res

        

if __name__ == "__main__":
    print(solution())
