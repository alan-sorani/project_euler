import itertools
import numpy as np

import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

def increment_sequence(sequence: list[int], max_vals: list[int], skip = False):
    """
    Increments the value of a sequence of numbers such that the value at the smallest index is increased by 1 if possible, or becomes 1 and carries over to the next index if not. If skip is True, instead set the left-most non-one value to 1 and increment the value following it by 1.

    Parameters
    ----------
    sequence: ndarray[int]
        A 1D ndarray of integers.
    max_vals: ndarray[int]
        A 1D ndarray of maximum possible values in the sequence, at the matching indices.
    Returns
    -------
    boolean
        False if the sequence cannot be incremented in the specified manner, otherwise True.
    """
    if((sequence == max_vals).all()):
        return False
    if(skip):
        temp_sequence = sequence.copy()
        skipped = False
        finished_skip = False
        for i in range(len(temp_sequence)-1):
            if(temp_sequence[i] != 1):
                skipped = True
                temp_sequence[i] = 1
                for j in range(i+1,len(temp_sequence)):
                    if(temp_sequence[j] == max_vals[j]):
                        temp_sequence[j] = 1
                    else:
                        temp_sequence[j] += 1
                        finished_skip = True
                        break
            if(skipped):
                if(finished_skip):
                    sequence[:] = temp_sequence.copy()
                return finished_skip
        return False

    for i in range(len(sequence)):
        if(sequence[i] == max_vals[i]):
            sequence[i] = 1
        else:
            sequence[i] += 1
            break
    return True

def find_four_consecutive_prime_products(num: int):
    primes = np.array(sieve_of_eratosthenes(num))
    four_prime_sets = list(itertools.combinations(primes, 4))
    num_sets = len(four_prime_sets)
    nums_found = set()
    res = None
    if(four_prime_sets == 0):
        return res
    for prime_set in four_prime_sets:
        if(np.prod(prime_set) > num):
            continue
        print(prime_set)
        max_powers = np.array([int(np.log(num)/np.log(prime)) for prime in prime_set])
        powers = np.array([1 for i in range(4)])
        i = 0
        stop = False
        
        while(stop == False):
            product = np.prod(prime_set ** powers)

            if(product > num):
                stop = not increment_sequence(powers, max_powers, skip=True)
                continue
            
            nums_found.add(product)
            if(
                    ({product - 3, product - 2, product - 1} <= nums_found) or
                    ({product - 2, product - 1, product + 1} <= nums_found) or
                    ({product - 1, product + 1, product + 2} <= nums_found) or
                    ({product + 1, product + 2, product + 3} <= nums_found)
            ):
                return product

            stop = not increment_sequence(powers, max_powers)
    return res

if __name__ == "__main__":
    large_num = 1000
    print(find_four_consecutive_prime_products(large_num))
