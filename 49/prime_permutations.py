import numpy as np
from itertools import permutations

def sieve_of_eratosthenes(num: int):
    """
    Returns a list of all prime numbers to up a given number.

    Parameters
    ----------
    num: int
        A positive integer.
    Returns
    -------
    list[int]
        A list of all the prime numbers up to num, using the sieve of eratosthenes method.
    """
    result = [True] * (num + 1) #binary array corresponding to numbers from 0 to num
    i = 2
    while(i < num):
        if (not result[i]):
            i = i + 1
            continue
        for j in range(i**2, num+1, i):
            result[j] = False
        i = i + 1
    return [i for i in range(2, num + 1) if result[i]]

def int_permutations(num : int):
    """
    Returns a list of numbers given by permuting the digits of a given integer.
    Parameters
    ----------
    num: int
        A positive integer.
    Returns
    -------
    list[int]
        A list of the positive integers given by permuting the digits of num.
    """
    return [int(''.join(perm)) for perm in permutations(str(num))]

def next_permutation(num : int):
    """
    Returns the minimal integer larger than num that is given by permuting the digits of num.

    Parameters
    ----------
    num : int
        A positive integer.
    Returns
    -------
    int
        The minimal integer larger than num that is given by permuting the digits of num, or 0 if there's no such integer.
    """
    permutations = int_permutations(num)
    larger_perms = [perm for perm in permutations if perm > num]
    return np.min(larger_perms) if larger_perms != [] else 0

primes = sieve_of_eratosthenes(9999)
primes = [prime for prime in primes if prime > 999]

res = []

for prime in primes:
    first_perm = prime
    while(first_perm != 0):
        first_perm = next_permutation(first_perm)
        if(first_perm not in primes):
            continue
        diff = first_perm - prime
        second_perm = first_perm + diff
        if(second_perm not in primes or second_perm not in int_permutations(prime)):
            continue
        res += [(prime, first_perm, second_perm)]

print(res)
