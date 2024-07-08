import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

from functools import cache
from time import time

@cache
def get_polygonal_sides(num : int):
    """
    Returns the possible numbers of sides between 4,5,6,7,8 for which a number is a polygonal number with that many sides.
    """
    res = set()
    for sides in range(4,9):
        if(get_polygonal_index(sides, num)[1]):
            res.add(sides)
    return res

def cycle_from(num : int):
    """
    Generates 4-digit integers where the first digits are the last two of num,
    and such that the third digit is non-zero.
    """
    num_str = str(num)
    first = num_str[2]
    second = num_str[3]
    for third in range(1,10):
        for fourth in range(10):
            yield int(''.join([first, second, str(third), str(fourth)]))

def polygonal_cycle_between(start : int,
                            end : int,
                            available_sides : set[int]
) -> list[int]:
    if(str(start)[2] == '0'):
        return False
    num_available_sides = len(available_sides)
    if(num_available_sides == 0):
        return []
    if(num_available_sides == 1):
        (sides,) = available_sides
        next_num = int(str(start)[2:] + str(end)[:2])
        if(get_polygonal_index(sides, next_num)[1]):
            return [next_num]
        return False
    for next_num in cycle_from(start):
        for sides in available_sides.intersection(get_polygonal_sides(next_num)):
            cycle_after = polygonal_cycle_between(next_num,
                                                  end,
                                                  available_sides - {sides})
            if(cycle_after):
                return [next_num] + cycle_after
    return False


def find_polygonal_cycle():
    first_index = get_polygonal_index(3, 1000)
    first_index = first_index[0] + (not first_index[1])
    last_index = get_polygonal_index(3,10000)
    last_index = last_index[0] + (not last_index[1])

    available_sides = {4,5,6,7,8}

    for i in range(first_index, last_index):
        num = polygonal_number(3,i)
        assert(num > 999 and num < 10000)
        cycle = polygonal_cycle_between(num, num, available_sides)
        if(cycle):
            return [num] + cycle
    return False

if __name__ == "__main__":
    time_start = time()
    cycle = find_polygonal_cycle()
    print(cycle)
    print(np.sum(cycle))
    time_end = time()
    print(f"Computed answer in {time_end - time_start} seconds.")
