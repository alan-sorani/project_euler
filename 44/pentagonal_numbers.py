import numpy as np
import itertools

'''
A number x is pentagonal if and only if there's an integer n such that :math:`x = n(3n-1)/2`. Moving x to the right-hand side and solving for n, we get that n must be :math:`\frac{1 + \sqrt{1 + 24x}}{6}`.
Hence, x is pentagonal if and only if :math:`\frac{1 + \sqrt{1 + 24x}}{6}` is an integer. 
'''

# we use the fact that p_n - p_{n-1} = 3n - 2 to define the iterator
def iter_pentagonal():
    p = 1
    d = 4
    while True:
        yield p
        p += d
        d += 3

def is_pentagonal(x : int):
    """
    Returns whether x is pentagonal.
    """
    sqrt_ = int(round(np.sqrt(1 + 24 * x)))
    return ((sqrt_ ** 2 == 1 + 24 * x) and (1 + sqrt_) % 6 == 0)

def solution() -> int:
    for p_sum in iter_pentagonal():
        for p_lower in iter_pentagonal():
            upper = p_sum - p_lower
            if upper < p_lower:
                break
            diff = upper - p_lower
            if is_pentagonal(upper) and is_pentagonal(diff):
                return diff

if(__name__ == "__main__"):
    print(solution())
