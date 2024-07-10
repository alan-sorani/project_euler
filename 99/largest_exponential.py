import numpy as np
from math import log

if __name__ == "__main__":
    with open("base_exp.txt", "r") as file:
        lines = file.readlines()
    max_pair = [2,1]
    max_index = 0

    lines = [line[:-1].split(",") for line in lines]
    lines = [[int(line[0]), int(line[1])] for line in lines]

    for i, line in enumerate(lines):
        base, exp = line
        adjusted_exp = exp * log(base) / log(max_pair[0])
        if(adjusted_exp > max_pair[1]):
            max_pair = [base, exp]
            max_index = i + 1
    print(max_pair, max_index)
