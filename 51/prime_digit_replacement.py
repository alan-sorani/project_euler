import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

from itertools import combinations,product

def replace_asterisks(num_str : str, digit : int) -> int:
    return int(num_str.replace("*", str(digit)))

def test_prime_replacements(num_str : str, target : int):
    count = 0
    for digit in [d for d in range(10)]:
        if(num_str[0] == "*" and digit == 0):
            continue
        if((count > target) or (count + 10 - digit < target)):
            return False
        num = replace_asterisks(num_str, digit)
        if(num in primes):
            count += 1
    return (count == target)


if __name__ == "__main__":
    max_power = 7
    primes = set(sieve_of_eratosthenes(10**max_power))
    digits = [d for d in range(1,10)]
    target = 8

    for num_digits in range(2,max_power):
        for num_replacements in range(1,num_digits):
            for other_indices in combinations(
                    range(0,num_digits-1),
                    num_digits - num_replacements - 1
                ):
                other_indices = list(other_indices) + [num_digits - 1]
                for other_digits in product(digits, repeat = num_digits - num_replacements):
                    num_str = np.array(["*" for i in range(num_digits)])
                    num_str[other_indices] = other_digits
                    num_str = ''.join(num_str)
                    if(test_prime_replacements(num_str, target)):
                        print(num_str)
                        exit()
