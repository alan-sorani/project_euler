import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

if __name__ == "__main__":
    for num in pandigitals(reverse = True):
        if(is_prime(num)):
            print(num)
            break
