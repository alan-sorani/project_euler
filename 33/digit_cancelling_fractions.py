import numpy as np
from sympy import Rational

def remove_digit(num : int, digit : int):
    """
    Returns a list of integers given from a specified integer by removing one instance of a given digit.
    """
    indices = [i for i,d in enumerate(str(num)) if int(d) == digit]
    return [int(str(num)[:i] + str(num)[i+1:]) for i in indices]

def digits(num : int):
    return set([int(digit) for digit in list(str(num))])

if __name__ == "__main__":
    numerator = 1
    denominator = 1
    for i in range(10,100):
        for j in range(i+1, 100):
            intersecting_digits = digits(i).intersection(digits(j))
            for digit in intersecting_digits:
                if(digit == 0):
                    continue
                for i_removed in remove_digit(i, digit):
                    for j_removed in remove_digit(j, digit):
                        if(i * j_removed == j * i_removed):
                            numerator *= i_removed
                            denominator *= j_removed
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break
    print(Rational(numerator,denominator))
                            

