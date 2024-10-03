import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import * 

import numpy as np
from fractions import Fraction

'''
We use the fundamental solution of the Pell's equation :math:`x^2 - n y^2 = 1`, as described on Wikipedia.
To find these solutions, we use the continued fraction expansion of :math:`\sqrt{n}` from problem 64, and use these to compute the convergents to it similarly to how we solved problem 65.
'''

def rewrite_fraction(num : int, a : int, b : int):
    """
    Returns coefficients for the fraction (c * sqrt(num) + d)/e which equals to a/(sqrt(num) + b).

    Parameters
    ----------
    num, a, b : int
        Integers.
    Returns
    -------
    tuple[int, int, int]
        Integers c,d,e such that sqrt(num) + c / d = a / (sqrt(num) + b).
    """
    return (int(-b), int((num-b**2)/a))

def continued_fraction_of_root(num : int) -> list[list[int], list[int]]:
    """
    Returns the continued fraction representation of the square root of a number, assuming the square root is irrational.

    Parameters
    ----------
    num : int
        A positive non-square integer.
    Returns
    -------
    list[list[int], list[int]]
        The numbers that appear in the representation of the square root of num as a continued fraction, where the numbers in the first list appear once and then the numbers in the second list repeat indefinitely.
    """
    res = []
    prev_coefficients = []
    c,d = (0,1)
    repeated = False
    repeat_start = 0

    while(not repeated):
        prev_coefficients += [(c,d)]
        int_part = int(np.floor((np.sqrt(num) + c)/d))
        res += [int_part]
        c -= int_part * d
        # take the coefficients c,d for the inverse of the previous fraction minus the integral part
        c,d = rewrite_fraction(num,d,c)
        if((c,d) in prev_coefficients):
            repeated = True
            repeat_start = prev_coefficients.index((c,d))
    res = [res[0:repeat_start], res[repeat_start:]]
    return res

def convergent_of_root(num : int, order : int, continued_fraction = None) -> Fraction:
    """
    Returns the convergent of the root of num with the given order of approximation.

    Parameters
    ----------
    num : int
        A positive non-square integer
    order : int
        The order of approximation for the convergent.
    continued_fraction : list[list[int], list[int]]
        The continued fraction representation for the square root of n.

    Returns
    -------
    Fraction
        The order'th convergent for the square root of num. If continued_fraction is passed, uses it as the continued fraction representation of the square root of n, instead of computing it again.
    """
    if(continued_fraction is None):
        continued_fraction = continued_fraction_of_root(num)
    if(order == 1):
        return continued_fraction[0][0]
    relevant_coefficients = continued_fraction[0]
    while(len(relevant_coefficients) < order):
        relevant_coefficients += continued_fraction[1]
    relevant_coefficients = relevant_coefficients[:order]
    first_coefficient = relevant_coefficients[0]
    reverse_coefficients = relevant_coefficients[1:][::-1]
    
    convergent = reverse_coefficients[0]
    i = 1
    while(i < len(reverse_coefficients)):
        convergent = Fraction(1, convergent)
        convergent += reverse_coefficients[i]
        i += 1
    convergent = Fraction(1, convergent)
    convergent += first_coefficient
    return convergent

def pell_fundamental_solution(n : int) -> [int, int]:
    """
    Returns the fundamental solution to the Diophantine Pell's equation :math:`x^2 - ny^2 = 1` where :math:`n` is a positive nonsquare integer.
    """
    continued_fraction = continued_fraction_of_root(n)
    p = len(continued_fraction[1])
    if(p % 2 == 0):
        convergent = convergent_of_root(n, p, continued_fraction)
    else:
        convergent = convergent_of_root(n, 2*p, continued_fraction)
    return (convergent.numerator, convergent.denominator)

def solution():
    x_max = 0
    arg_max = 0

    for D in range(1, 1001):
        if(D == int(np.sqrt(D))**2):
            continue
        x,y = pell_fundamental_solution(D)
        if(x > x_max):
            x_max = x
            arg_max = D
    return arg_max

if __name__ == "__main__":
    print(solution())
