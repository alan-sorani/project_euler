import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

digits = [str(i) for i in range(10)]

def are_permutations(num_1 : int, num_2 : int):
    str_1 = str(num_1)
    str_2 = str(num_2)
    for digit in digits:
        if(str_1.count(digit) != str_2.count(digit)):
            return False
    return True

def solution():
    max_digits = 16
    target = 5

    for num_digits in range(1,max_digits+1):
        min_root = int(10**((num_digits-1)/3))
        max_root = int(10**(num_digits/3))
        cubes = [i**3 for i in range(min_root-100, max_root+100) if (i**3 >= 10**(num_digits - 1) and i**3 <= 10**num_digits)]
        while(len(cubes) != 0):
            cube = cubes[0]
            cube_permutations = set()
            for other_cube in cubes:
                if(are_permutations(cube, other_cube)):
                    cube_permutations.add(other_cube)
            num_permutations = len(cube_permutations)
            if(num_permutations == target):
                return cube
            cubes = list(set(cubes) - cube_permutations)
            cubes.sort()
    return -1


if __name__ == "__main__":
    res = solution()
    print(res)
