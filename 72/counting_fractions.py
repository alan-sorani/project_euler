import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)

from number_utils import *
from combinatorics_utils import *
import numpy as np
import timeit

'''
We want to sum phi(d) over d between 2 and 10**6, where phi(n) is Euler's totient function.

This equals Phi(10**6) - 1 where Phi is the totient summatory function, namely :math:`\Phi(n) \coloneqq \sum_{k=1}^n \phi(k)`.

Using Mobius inversion, we have
:math:`\Phi(n) = \frac{1}{2} \sum_{k=1}^n \mu(k) \floor{\frac{n}{k}} \left( 1 + \floor{\frac{n}{k}} \right)`, where :math:`\mu` is the Mobius function, being 0 for numbers that aren't square-free, and -1 to the number of prime factors otherwise.
'''

def totient_summatory_function(n : int):
    primes = np.array(sieve_of_eratosthenes(n))
    num_primes = len(primes)
    res = n * (n+1)
    count = 0

    for num_factors in range(1, len(primes) + 1):
        if(np.prod(primes[:num_factors]) > n):
            break
        mu = (-1)**num_factors
        unsigned_summands = 0
        
        factor_indices = [i for i in range(num_factors)]
        skip = 0
        stop = False
        while(not stop):
            k = int(np.prod(primes[factor_indices]))

            if(k > n):
                skip += 1
                if(skip >= len(factor_indices)):
                    break
            else:
                skip = 0
                quot_floor = int(np.floor(n/k))
                unsigned_summands += quot_floor * (1 + quot_floor)

            stop = not increment_sublist_index(factor_indices, num_primes - 1, skip)

        res += mu * unsigned_summands
        
    return res / 2
        
def solution():
    return (totient_summatory_function(10**6) - 1)

if __name__ == "__main__":
    timeit_runs = 10
    solution_time = timeit.timeit(lambda: solution(), number=timeit_runs)
    print(f"Found solution {solution()} in {solution_time} seconds on average across {timeit_runs} runs.")
