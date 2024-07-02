import numpy as np
from numpy import floor,sqrt
from itertools import permutations

def pandigitals(reverse : False):
    """
    Creates a generator for pandigital numbers.
    """
    num_digits = 9 if reverse else 1
    while(num_digits > 1):
        digits = ''.join([str(d) for d in range(1, num_digits + 1)])
        perms = list(permutations(digits))
        if(reverse):
            perms = perms[::-1]
        for perm in perms:
            yield int(''.join(perm))
        num_digits += (-1) if reverse else 1

def is_prime(n : int):
    result = True
    i = 1
    while(result == True and i<floor(sqrt(n))):
        i+=1
        if(n/i == int(n/i)):
            result = False
    return result


if(__name__ == "__main__"):
    for num in pandigitals(reverse = True):
        print(num)
