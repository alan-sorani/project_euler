import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

from itertools import permutations

cubes_to_skip = set()

def digit_permutations(num : int):
    num_str = str(num)
    for permutation in set(permutations(num_str)):
        num_str = ''.join(permutation)
        res = int(num_str)
        if(res >= num):
            yield res

def test_cubic_permutations(num : int, num_permutations : int) -> bool:
    count = 0
    for perm in digit_permutations(num):
        root = int(np.round(perm**(1/3)))
        if(root ** 3 == perm):
            count += 1
            if(perm != num):
                cubes_to_skip.add(perm)
        if(count > num_permutations):
            return False
    return (count == num_permutations)

def find_cube_with_cubic_permutations():
    n = 0
    found = False
    while(not found):
        n += 1
        cube = n**3
        if(cube in cubes_to_skip):
            cubes_to_skip.remove(cube)
            continue
        found = test_cubic_permutations(n**3, 5)
    return n**3


if __name__ == "__main__":
    print(find_cube_with_cubic_permutations())
