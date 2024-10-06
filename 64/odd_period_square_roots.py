import numpy as np

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

def continued_fraction_of_root(num : int):
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

count = 0

for num in range(10001):
    if(num != int(np.round(np.sqrt(num)))**2):
        odd_period = (len(continued_fraction_of_root(num)[1]) % 2 != 0)
        count += odd_period

print(count)

