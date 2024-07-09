import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

if __name__ == "__main__":
    with open("keylog.txt", "r") as file:
        lines = file.readlines()
    keys = [list(line)[:-1] for line in lines]
    numbers_after = dict([(str(i), []) for i in range(10)])
    password = ""
    for key in keys:
        try:
            first_index = password.index(key[0])
        except ValueError:
            first_index = None
