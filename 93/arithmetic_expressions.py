import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from combinatorics_utils import *

from itertools import combinations

def get_arithmetic_combinations(digits : list[int]) -> list[int]:
    if(len(digits) == 1):
        return digits

    res = []
    for partition in partitions(digits, 2):
        expressions_1 = get_arithmetic_combinations(partition[0])
        expressions_2 = get_arithmetic_combinations(partition[1])
        for a in expressions_1:
            for b in expressions_2:
                res += [a + b, a - b, b - a, a * b]
                if(b != 0):
                    res += [a/b]
    res = list(set(res))
    res.sort()
    return res

def get_integer_arithmetic_combinations(digits : list[int]) -> list[int]:
    combs = get_arithmetic_combinations(digits)
    combs = [int(comb) for comb in combs if comb == int(comb) and comb > 0]
    return combs

if __name__ == "__main__":
    max_length = 0
    res = []

    for digits in combinations(range(1,10),4):
        digits = list(digits)
        combs = get_integer_arithmetic_combinations(digits)
        chain_length = min([i for i in range(len(combs)) if combs[i] != i+1])
        if(chain_length > max_length):
            max_length = chain_length
            res = digits
            print(digits, max_length, combs)
    print()
    print(max_length, res)
