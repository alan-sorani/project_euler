import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from combinatorics_utils import sums_of_naturals

if(__name__ == "__main__"):
    print(sums_of_naturals(100, order = False)-1)
