import numpy as np

import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

'''
We want m such that the concatenation of m*1, m*2, ..., m*n for some positive integer n, is a pandigital number.

If m has 3 digits, m*1 has 3 digits and m*2 has at most 4 digits, so the concatenation would have 7 digits. Hence we need n >= 3. But, m*k will always have at least 3 digits, so n = 3. We need also m * 3 = m * n <= 999, so m <= 333.

If m has 4 digits and m*2 also has 4 digits, their concatenation has 8 digits, which is too little, and concatenating also with m*3 will have too many digits. Hence, if m has 4 digits, we need m >= 5000.

If m has 5 or more digits, so does m*2, so concatenating those will give too many digits.
'''

def is_pandigital(num : int):
    num_string = str(num)
    return (len(num_string) == 9 and set(num_string) == set("123456789"))

def concatenate_integers(integer_list : list[int]):
    return int(''.join([str(integer) for integer in integer_list]))

if __name__ == "__main__":
    max_pandigital_multiple = 0
    for i in set(range(1,100)).union(set(range(100,334))).union(set(range(5000,10000))):
        for n in range(2,9):
            multiple = concatenate_integers([j * i for j in range(1,n+1)])
            if(
                multiple > max_pandigital_multiple and
                is_pandigital(multiple)
            ):
                max_pandigital_multiple = multiple

    print(max_pandigital_multiple)
