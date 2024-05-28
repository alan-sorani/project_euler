from math import log

first_primes = [1,2,3,5,7,11]

"""
nth_prime

Input: an integer n
Output: the nth prime number
"""

def nth_prime(n):
    if(n<6):
        return first_primes[n]
    upper_bound = n * (log(n) + log(log(n)))
    i = 1
    candidates = [i for i in range(2,int(upper_bound)+1)]
    while(True):
        ith_prime = candidates[0]
        if(i == n):
            return ith_prime
        i = i + 1
        candidates = [n for n in candidates if n % ith_prime != 0]
    
