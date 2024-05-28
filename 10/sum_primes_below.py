import numpy as np

def sieve_of_eratosthenes(num):
    """
    sieve_of_eratosthenes

    Input: a number, num
    Output: an array of all the prime numbers up to num, using the sieve of eratosthenes method
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


"""
sum_primes_below

    Input: a number, num
    Output: the sum of all numbers below 
"""

def sum_primes_below(num): 
    return np.sum(sieve_of_eratosthenes(num-1))
