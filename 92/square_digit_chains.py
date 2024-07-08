import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

import numpy as np

def sum_squared_digits(num : int):
    return np.sum([int(digit)**2 for digit in str(num)])

if __name__ == "__main__":
    large_num = 10**7
    ends = {1:1, 89:89}
    for i in range(1,large_num):
        if(i in ends):
            continue
        chain = []
        temp = i
        while(temp not in ends):
            chain += [temp]
            temp = sum_squared_digits(temp)
        for num in chain:
            ends[num] = ends[temp]
    numbers = [i for i in ends if ends[i] == 89 and i < large_num]
    for i in {44,32,13,10}:
        assert(ends[i] == 1)
    for i in {145,42,20,4,16,37,58}:
        assert(ends[i] == 89)
    res = len(numbers)
    print(res)
