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
    Computes the Gaussian bracket :math:`[n]_q` defined as the Gaussian binomial coefficient :math:`\binom{m}{r}_q`.

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
