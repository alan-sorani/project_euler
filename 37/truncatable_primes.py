import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

def truncate_left(num : int):
    if(num <= 9):
        raise ValueError("Givne integer is too small to be truncated.")
    return int(str(num)[1:])

def truncate_right(num : int):
    if(num <= 9):
        raise ValueError("Givne integer is too small to be truncated.")
    return int(str(num)[:-1])

if __name__ == "__main__":
    large_num = 10**7
    res = 0
    truncatable_primes = []
    primes = set(sieve_of_eratosthenes(large_num))
    for prime in primes:
        if(prime < 10):
            continue
        left_truncated = prime
        right_truncated = prime
        while(left_truncated > 9):
            left_truncated = truncate_left(left_truncated)
            right_truncated = truncate_right(right_truncated)
            if(not({left_truncated, right_truncated} <= primes)):
                break
        else:
            res += prime
            truncatable_primes += [prime]
    print(res, truncatable_primes)
    
