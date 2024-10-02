import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from number_utils import *

from time import time
from collections import defaultdict
from itertools import combinations

def is_prime_pair(first : int, second : int) -> bool:
    concat_1 = int(str(first) + str(second))
    concat_2 = int(str(second) + str(first))
    return (concat_1 in prime_set or miller_rabin(concat_1)) and (concat_2 in prime_set or miller_rabin(concat_2))

def find_prime_pair_set(size : int) -> list[int]:
    # We go over the maximum prime in the candidate set, and notice that every other prime in the set should be such that concatenating these two primes results in a prime number.
    min_sum = float('inf')
    smaller_partners = defaultdict(list)
    for first_prime in primes:
        if(first_prime > min_sum):
            break
        for second_prime in primes:
            if(second_prime == first_prime):
                break
            if(is_prime_pair(first_prime, second_prime)):
                smaller_partners[first_prime] += [second_prime]
        if(len(smaller_partners[first_prime]) >= size - 1):
            for partner_subset in combinations(
                smaller_partners[first_prime],
                size - 1):
                if(sum(partner_subset) + first_prime >= min_sum):
                    break
                for i, number in enumerate(partner_subset):
                    for other_number in partner_subset[:i]:
                        if(other_number not in smaller_partners[number]):
                            break
                    else:
                        continue
                    break
                else:
                    min_sum = min(min_sum, sum(partner_subset) + first_prime)
    return min_sum

if __name__ == "__main__":
    time_0 = time()

    primes = sieve_of_eratosthenes(10**6)
    prime_set = set(primes)
    sum = find_prime_pair_set(5)

    diff_time = time() - time_0
    print(sum)
    print(f"Computed in {diff_time} seconds.")
