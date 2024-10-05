import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)

from number_utils import *
from combinatorics_utils import *
import numpy as np

'''
We want to sum phi(d) over d between 2 and 10**6, where phi(n) is Euler's totient function.

This equals Phi(10**6) - 1 where Phi is the totient summatory function, namely :math:`\Phi(n) \coloneqq \sum_{k=1}^n \phi(k)`.

Using Mobius inversion, we have
:math:`\Phi(n) = \frac{1}{2} \sum_{k=1}^n \mu(k) \floor{\frac{n}{k}} \left( 1 + \floor{\frac{n}{k}} \right)`, where :math:`\mu` is the Mobius function, being 0 for numbers that aren't square-free, and -1 to the number of prime factors otherwise.
'''

def solution():
    n = 10**6
    primes = np.array(sieve_of_eratosthenes(n))
    num_primes = len(primes)
    res = 0
    
    for num_primes in range(1, len(primes)):
        if(np.prod(primes[:num_primes]) > n):
            break
        mu = 1 if (num_primes % 2 == 0) else -1
        unsigned_summands = 0
        
        factor_indices = [i for i in range(num_primes)]
        skip = 0
        stop = False
        while(not stop):
            print(factor_indices)
            k = int(np.prod(primes[factor_indices]))

            if(k > n):
                skip += 1
                if(skip >= len(factor_indices)):
                    break

            else:
                skip = 0
                quotient_floor = int(np.floor(n/k))
                unsigned_summands += quotient_floor * (1 + quotient_floor)

            stop = not increment_sublist_index(factor_indices, num_primes - 1, skip)

        res += mu * unsigned_summands
        
    res = res / 2
    return res
        

if __name__ == "__main__":
    print(solution())
