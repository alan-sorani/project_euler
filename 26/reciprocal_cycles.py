import numpy as np

def reciprocal_division(n):
    """
    Divides 1/n using long division, denoting possible recurring digits in the fractional part inside parenthesis.

    Parameters
    ----------
    n : int
        A positive integer greater than 1.
    Returns
    -------
    str
        A decimal representation of the fraction 1/n, where repeating digits in the fractional part are denoted in parentheses.
    """
    digits = []
    numerator = 10
    previous_numerators = [10]
    repeat_start = -1
    repeated = False

    while((numerator != 0) and (not repeated)):
        while(numerator < n):
            numerator *= 10
            digits += [0]
            previous_numerators += [numerator]
        digits += [numerator // n]
        numerator = numerator - digits[-1] * n
        numerator *= 10
        repeated = (numerator in previous_numerators)
        if(repeated):
            break
        previous_numerators += [numerator]
    if(repeated):
        repeat_start = previous_numerators.index(numerator)+1
    
    res = "."
    for digit in digits:
        res += f"{digit}"
    if(repeat_start != -1):
        res = res[:repeat_start] + "(" + res[repeat_start:] + ")"
    return res

def reciprocal_cycle(n):
    """
    Returns a list of the digits in the recurring cycle of the fraction 1/n, or an empty list if there's no recurring cycle.
    
    Parameters
    ----------
    n: int
        A positive integer greater than 1.
    Returns
    -------
    list[int]
        A list containing the digits in the recurring cycle of the fraction 1/n, or an empty list if there are no recurring digits.
    """
    str_frac = reciprocal_division(n)
    if(chr(40) not in str_frac):
        return []
    start_index = str_frac.index(chr(40)) + 1
    digits = str_frac[start_index : - 1]
    return [int(digit) for digit in digits]

max_length = 0
max_index = -1
for i in range(2,1000):
    length = len(reciprocal_cycle(i))
    if(length > max_length):
        max_length = length
        max_index = i
print(max_index)
