from math import floor, sqrt

"""

is_prime

Input: an integer n
Output: True if n is prime and False otherwise

"""

def is_prime(n):
    result = True
    i = 1
    while(result == True and i<=floor(sqrt(n))):
        i+=1
        if(n/i == int(n/i)):
            result = False
    return result

"""
largest_prime_factor

Input: an integer n
Output: the largest prime factor of n
"""

def largest_prime_factor(n):
    k = floor(sqrt(n))
    while(n/k != int(n/k) or is_prime(k) == False):
        k -= 1
    return k
