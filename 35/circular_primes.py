import numpy as np

def sieve_of_eratosthenes(num):
    """
    sieve_of_eratosthenes

    Input: a number, num
    Output: an array of all the prime numbers up to num, using the sieve of eratosthenes method
    """
    result = [True] * (num + 1) #binary array corresponding to numbers from 0 to num
    i = 2
    while(i < num):
        if (not result[i]):
            i = i + 1
            continue
        for j in range(i**2, num+1, i):
            result[j] = False
        i = i + 1
    return [i for i in range(2, num + 1) if result[i]]

def circular_permutations(list_):
    temp_list = list_[:]
    repeated = False
    length = len(list_)
    for i in range(length):
        yield tuple(temp_list)
        temp_list = temp_list[-1] + temp_list[:-1]


def count_circular_primes_up_to(num : int):
    primes = set(sieve_of_eratosthenes(num))
    count = 0
    counted = []
    for prime in primes:
        if prime in counted:
            continue
        perms = set([int(''.join(perm)) for perm in circular_permutations(str(prime))])
        if(perms <= primes):
            counted += list(perms)
            count += len(perms)
    return count

if __name__ == "__main__":
    print(count_circular_primes_up_to(10**6))

