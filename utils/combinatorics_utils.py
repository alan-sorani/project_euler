import numpy as np
import sympy
from numpy import pi
from math import comb as binom
from math import factorial
from sympy import var, I
from sympy.polys.polytools import poly_from_expr
from typing import Callable
from functools import cache

def polynomial_coefficients(
        p : Callable[[np.complex64], np.complex64],
        deg : int,
        precision : int
    ):
    """
    Computes the coefficients of a polynomial given as a function, given its degree.

    Parameters
    ----------
    p : function
        A polynomial function.
    deg : int
        The degree of the polynomial.
    precision : num
        The precision for the coefficient calculaiton, being the number of significant digits.

    Returns
    -------
    list[int]
        A list containing the coefficients of the polynomial.
    
    Notes
    -----
    This computes the coefficients using the Fast-Fourier-Transform method.
    """

    exp_func = lambda k : np.exp(np.complex64(0,-(2 * pi * k)/(deg + 1)))
    X = [p(exp_func(k)) for k in range(deg+1)]
    res = []
    for i in range(deg + 1):
        res += [np.sum([X[k] * exp_func(-i*k) for k in range(deg+1)]) / (deg + 1)] 
        res[i] = np.complex64(np.round(res[i],precision))
    return res

def expression_to_polynomial(
        expression : sympy.core.add.Add,
        var : sympy.core.symbol.Symbol,
        deg : int,
        precision : int
    ):
    f = lambda x : np.complex64(expression.subs(var,x))
    coefficients = polynomial_coefficients(
                f,
                deg,
                precision
            )
    res = 0
    for i in range(deg + 1):
        res += coefficients[i] * var**i
    return res

def gaussian_bracket(n : int):
    """
    Computes the Gaussian bracket [n]_k.

    Paremeters
    ----------
    n : int
        An integer.
    
    Returns
    -------
    sympy.core.add.Add 
        The polynomial :math:`\sum_{0 \leq i < n} q^i`, where :math:`q` is an indeterminate.
    """
    q = var('q')
    res = 0
    for i in range(n):
        res += q**i           
    return res

def gaussian_binomial(n : int, k : int, reduced = False):
    """
    Computes the Gaussian binomial coefficient (n, k)_q.

    Parameters
    ----------
    n,k : int
        Two non-negative integers.
    reduced : boolean
        A boolean value determining reduction of the polynomial expression.
    
    Returns
    -------
    tuple[sympy.core.add.Add,int]
        A tuple containing the Gaussian binomial coefficient (n,k)_q and its the degree. The polynomial is in the indeterminate q.
        If reduced is True, return the expression written as a polynomial.
    """
    if(reduced):
        binomial = gaussian_binomial(n, k)
        return expression_to_polynomial(binomial[0], var('q'), binomial[1], 3)
    binomial = 1
    for i in range(k):
        binomial *= (gaussian_bracket(n - i) / gaussian_bracket(i + 1))
    return (binomial, k * (n - k))

@cache
def sums_of_k_naturals_no_order(num : int, k : int, max_summand : int):
    if (k < 1):
        return 0
    if (num in {0,1}):
        return 1
    if (k == 1):
        return (num <= max_summand)
    result = 0
    # iterate over the highest number in the sum
    for i in range(1, max_summand+1):
        new_max_summand = np.min([num - i, i])
        result += sums_of_k_naturals_no_order(num-i, k-1, new_max_summand)
    return result

def sums_of_k_naturals(
        num : int,
        k : int,
        order = False,
        zeros = False
    ):
    """
    Returns the number of ways to write a given number as the sum of natural numbers.
    
    Parameters
    ----------
    num : int
        A natural number.
    k : int
        A natural number.
    order : boolean
        A boolean value determening if the program counts different orders of the same values.
    zeros : boolean
        A boolean value determining if the program counts 0 as being an optional value.

    Returns
    -------
    int
        The number of ways to write n as the sum of k natural numbers. If order = True, the ordering of the numbers matters, otherwise it doesn't. If zeros = False, zeros cannot appear in the sum.
    """
    
    '''
    If we consider the stars-and-bars method, dividing stars between the bars such that there aren't zeros is the same as dividing k fewer stars.
    '''
    num -= k * (not zeros)

    if(order):
        return binom(num + k - 1, k - 1)
    else:
        return sums_of_k_naturals_no_order(num, k, num)

        '''
        less efficient method:
        
        return gaussian_binomial(
                    num + k, k, reduced = True
                ).coeff(var('q')**num)
        '''

@cache
def sums_of_naturals_no_order(num : int, max_summand : int):
    if num in {0,1}:
        return num
    # count 1 if the number is allowed to be written as itself
    result = (num <= max_summand)
    # iterate over the highest number in the sum
    for i in range(1, max_summand+1):
        new_max_summand = np.min([num - i, i])
        result += sums_of_naturals_no_order(num-i, new_max_summand)
    return result


def sums_of_naturals(
        num : int,
        order = False
    ):
    """
    Returns the number of ways to write a given number as the sum of natural numbers.
    
    Parameters
    ----------
    num : int
        A natural number.
    order : boolean
        A boolean value determening if the program counts different orders of the same values.

    Returns
    -------
    int
        The number of ways to write n as the sum of natural numbers. If order = True, the ordering of the numbers matters, otherwise it doesn't.
    """
    if(not order): 
        return sums_of_naturals_no_order(num, num)
    
    res = 0
    for k in range(1, num + 1):
        res += sums_of_k_naturals(
                    num = num,
                    k = k,
                    order=True,
                    zeros=False
                )
    return res

if __name__ == "__main__":
    print(sums_of_k_naturals(10,3,order=False,zeros=True))

