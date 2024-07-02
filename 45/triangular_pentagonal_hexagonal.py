import numpy as np

'''
We already have a function that checks if a number is triangular, from Problem 42.

We write a function to chek if a number is hexagonal, then generated pentagonal numbers and check if they're triangular and hexagonal.
'''

def is_triangular(num : int):
    """
    Checks whether a given positive integer is triangle.

    Parameters
    ----------
    num : int
        A positive integer.

    Returns
    -------
    True if num is a triangle number, or False otherwise.

    Notes
    -----
    A triangle number is of the form :math:`t_n \coloneqq n(n+1)/2` for a positive integer n. Expressing n from this equation we get that it equals :math:`\frac{-1 \pm \sqrt(1 + 8 t_n)}{2}, so a number m is a triangle number if and only if 1 + 8m is a square.
    """
    temp = 1 + 8 * num
    return np.round(np.sqrt(temp)) ** 2 == temp


def is_hexagonal(num : int):
    """
    Checks whether a given positive integer is triangle.

    Parameters
    ----------
    num : int
        A positive integer.

    Returns
    -------
    True if num is a triangle number, or False otherwise.

    Notes
    -----
    An hexagonal number is of the form :math:`h_n \coloneqq n(2n-1)` for a positive integer n. Expressing n from this equation we get that it equals :math:`\frac{1 \pm \sqrt(-1 + 8 h_n)}{4}, so a number m is hexagonal if and only if -1 + 8m is a square and 1 + sqrt(-1 + 8m) is divisible by 4.
    """
    temp = int(1 + 8 * num)
    sqrt = int(np.round(np.sqrt(temp)))
    return ((sqrt ** 2 == temp) and ((1 + sqrt) % 4 == 0))

if __name__ == "__main__":
    n = 166
    while(True):
        pentagonal = int(n * (3*n - 1) / 2)
        if(is_triangular(pentagonal) and is_hexagonal(pentagonal)):
            break
        n += 1
    print(n, pentagonal)
