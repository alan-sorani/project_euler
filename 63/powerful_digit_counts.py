import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

from math import log
import numpy as np

'''
Doing a bit of arithmetic, we see that for a digit d, d^n has n digits if and only if 1/10 <= (d/10)^n. This is equivalent to n <= log_{d/10}{1/10}, where the latter equals -1/(log_{10}(d) - 1).
We count the number of options for that.
'''

if __name__ == "__main__":
    count = 0
    for d in range(1,10):
        count += np.floor(-1 / (log(d)/log(10) - 1)) 
    print(count)
