import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

large_num = 10**6
primes = sieve_of_eratosthenes(large_num * 10)
twice_squares = [2 * i**2 for i in range(large_num)]

if __name__ == "__main__":
    i = 9
    res = None
    while(True):
        if(i > large_num):
            large_num *= 100
            primes = sieve_of_eratosthenes(large_num * 10)
            twice_squares = [2 * i**2 for i in range(1, large_num)]
        if(is_prime(i)):
            i += 2
            continue
        for prime in primes:
            if(prime > i):
                res = i
                break
            if((i - prime) in twice_squares[:i]):
                i += 2
                break
        if(res != None):
            print(res)
            break
