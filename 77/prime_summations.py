import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from combinatorics_utils import PositiveIntSet
from number_utils import sieve_of_eratosthenes 

if __name__ == "__main__":
    primes = sieve_of_eratosthenes(10**6)
    int_set = PositiveIntSet(set(primes))
    i = 2
    res = 0
    while(res <= 5000):
        res = int_set.sums_no_order(i)
        i += 1
    print(i-1)
