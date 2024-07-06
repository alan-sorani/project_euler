import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from combinatorics_utils import *

if __name__ == "__main__":
    int_set = PositiveIntSet({1,2,5,10,20,50,100,200})
    print(int_set.sums_no_order(200))
