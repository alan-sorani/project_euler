import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)

from number_utils import *

'''
We notice that the number of fractions between 1/3 and 1/2 is the number of fractions up to 1/2 minus the number of fractions up to 1/3, minus 1.
It therefore suffices to find the number of fractions up to 1/n for every positive integer n.
'''

def solution():
    return (totient_summatory_function(10**6) - 1)

if __name__ == "__main__":
    timeit_runs = 10
    solution_time = timeit.timeit(lambda: solution(), number=timeit_runs)
    print(f"Found solution {solution()} in {solution_time} seconds on average across {timeit_runs} runs.")
