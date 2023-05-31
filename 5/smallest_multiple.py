from math import floor, sqrt, log

"""

is_prime

Input: an integer n
Output: True if n is prime and False otherwise

"""

def is_prime(n):
    result = True
    i = 1
    while(result == True and i<floor(sqrt(n))):
        i+=1
        if(n/i == int(n/i)):
            result = False
    return result

"""
smallest_multiple

Input: an integer n
Output: the smallest multiple of all positive integers up to n
"""

def smallest_multiple(n):
    result = 1
    for i in range(2,n+1):
        if is_prime(i):
            result*=i**(floor(log(n,i)))
    return result
