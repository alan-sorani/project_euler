import numpy as np
from numpy import floor, sqrt

def is_prime(n : int):
    """
    Returns whether a given positive integer is prime.

    Parameters
    ----------
    n : int
        A positive integer.
    Returns
    -------
    boolean
        True if n is prime, otherwise False.
    """
    result = True
    i = 1
    while(result == True and i<floor(sqrt(n))):
        i+=1
        if(n/i == int(n/i)):
            result = False
    return result

def count_quadratic_primes(a : int, b : int):
    """
    Counts how many consecutive values of n^2 + an + b are primes, starting with n = 0.
    
    Parameters
    ----------
    a,b : int
        Coefficients of the polynomial to be checked.
    Returns
    -------
    int
        The number of consecutive values of n^2 + an + b that are primes, starting with n = 0.
    """
    n = 0
    p = lambda x : x**2 + a * x + b
    res = 0
    num = b
    while(num > 0 and is_prime(num)):
        res += 1
        n += 1
        num = p(n)
    return res

max_coefficients = (0,0)
max_sequence_length = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        sequence_length = count_quadratic_primes(a,b)
        if(sequence_length > max_sequence_length):
            max_sequence_length = sequence_length
            max_coefficients = (a,b)

print(max_sequence_length, max_coefficients)
