import numpy as np

def num_divisors(n: int):
    """
    The number of divisors of a number n.

    Parameters
    __________
    n: int
        The number to count divisors of.

    Returns
    _______
    int
        The number of divisors of the parameter n.
    """
    res = 0
    i = 1
    while(i ** 2 <= n):
        if(n % i == 0):
            res += 2
        i += 1
    if((i-1)**2 == n):
        res -= 1
    return res

def triangular_number_divisors(n: int):
    """
    The number of divisors for the n'th triangular number.

    Parameters
    ----------
    n: int
        The index of the triangular number to count divisors for.

    Returns
    -------
    int
        The number of divisors for the n'th triangular number, which is the sum of the first n positive integers.
    """
    if(n % 2 == 0):
        return num_divisors(n/2) * num_divisors(n+1)
    else:
        return num_divisors(n) * num_divisors((n+1)/2)

def triangular_number(n: int):
    """
    The n'th triangular number.

    Parameters
    ----------
    n: int
        The index of the triangular number to be returned.
    Returns
    -------
    int
        The n'th triangular number.
    """
    return n * (n+1) / 2

def highly_divisible_triangular_number(min_num_divisors: int):
    """
    The first triangular number to have at least a certain number of divisors.
    
    Parameters
    ----------
    min_num_divisors: int
        The minimum number of divisors for the result triangular number to have.
    Returns
    -------
    int
        The first triangular number to have at least min_num_divisors divisors.
    """
    i = 1
    while(True):
        if(triangular_number_divisors(i) >= min_num_divisors):
            break
        i += 1
    return triangular_number(i)
