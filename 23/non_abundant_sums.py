"""
We use our functions from problem 21 to find the divisors of all numbers up to 28123 and check if they're abundant. Then we check which numbers up to 28123 are sums of two abundant numbers, and we sum the rest of the numbers up to 28123.
"""

import numpy as np
import itertools

def index_iterator(shape):
    """
    Returns an iterator of indices for an array of the given shape.

    Parameters
    ----------
    shape: tuple[int, ..., int] or list[int, ..., int]
        The shape of an array.
    Returns
    -------
    iterator[tuple[int]]
        An iterator containing the indices of an array of the given shape.
    """
    ranges = [range(dim) for dim in shape]
    product = itertools.product(*ranges)
    return product

def sieve_of_eratosthenes(num: int):
    """
    Returns a list of all prime numbers to up a given number.

    Input: an integer, num
    Output: a list of all the prime numbers up to num, using the sieve of eratosthenes method
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

def increment_sequence(sequence: list[int], max_vals: list[int], skip = False):
    """
    Increments the value of a sequence of numbers such that the value at the smallest index is increased by 1 if possible, or becomes 0 and carries over to the next index if not. If skip is True, instead set the left-most non-zero value to 0 and increment the value following it by 1.

    Parameters
    ----------
    sequence: ndarray[int]
        A 1D ndarray of integers.
    max_vals: ndarray[int]
        A 1D ndarray of maximum possible values in the sequence, at the matching indices.
    Returns
    -------
    boolean
        False if the sequence cannot be incremented in the specified manner, otherwise True.
    """
    if((sequence == max_vals).all()):
        return False
    if(skip):
        temp_sequence = sequence.copy()
        skipped = False
        finished_skip = False
        for i in range(len(temp_sequence)-1):
            if(temp_sequence[i] != 0):
                skipped = True
                temp_sequence[i] = 0
                for j in range(i+1,len(temp_sequence)):
                    if(temp_sequence[j] == max_vals[j]):
                        temp_sequence[j] = 0
                    else:
                        temp_sequence[j] += 1
                        finished_skip = True
                        break
            if(skipped):
                if(finished_skip):
                    sequence[:] = temp_sequence.copy()
                return finished_skip
        return False

    for i in range(len(sequence)):
        if(sequence[i] == max_vals[i]):
            sequence[i] = 0
        else:
            sequence[i] += 1
            break
    return True

def factorize_up_to(num: int):
    """
    Returns a dictionary with keys being all the numbers up to num, and the values are the factorizations of these numbers.

    Parameters
    ----------
    num: int
        A positive integer.
    Returns
    -------
    A dictionary with keys are the positive integers up to num, and the values are their prime factorizations, as a list [(p_1, k_1), ..., (p_m, k_m)] where the number is the product of p_i^{k_i}.
    """
    primes = np.array(sieve_of_eratosthenes(num))
    num_primes = len(primes)
    res = {1: []}
    if(num_primes == 0):
        return res
    max_powers = np.array([int(np.log(num)/np.log(prime)) for prime in primes])
    powers = np.array([0 for i in range(num_primes)])
    increment_sequence(powers, max_powers)
    i = 0
    stop = False

    while(stop == False):
        product = np.prod(primes ** powers)
        if(product > num):
            stop = not increment_sequence(powers, max_powers, skip=True)
            continue
        res[product] = [(prime,power) for prime,power in zip(primes,powers) if power > 0]
        stop = not increment_sequence(powers, max_powers)

    return res

def factorization_to_divisors(factorization: list[tuple[int,int]]):
    """
    Takes a factorization of a number as outputted by factorize_up_to and returns a list of the number's divisors.

    Parameters
    ----------
    factorization: list[tuple[int,int]]
        A factorization of a positive integer, as outputted by factorize_up_to.
    Returns
    -------
    list[int]
        A list of the number's divisors.
    """
    res = []
    length = len(factorization)
    if(length == 0):
        return [1]
    primes = [factorization[i][0] for i in range(length)]
    shape = [factorization[i][1]+1 for i in range(length)]
    list_powers = index_iterator(shape = shape)
    for powers in list_powers:
        res += [np.prod(np.array(primes) ** np.array(powers))]
    return res

def divisors_up_to(num: int):
    """
    Returns a dictionary with keys being all the numbers up to num, and the value for each number is a list of its divisors.

    Parameters
    ----------
    num: int
        A positive integer.
    Returns
    -------
    dict[int, list[int]]
        A dictionary with keys being all the positive integers up to num, and the value for each number is a list of its divisors.
    """
    divisors = {}
    factorizations = factorize_up_to(num)
    for key,value in factorizations.items():
        divisors[key] = factorization_to_divisors(value)
    return divisors

def abundant_numbers_up_to(num: int):
    """
    Returns a list of all the abundant numbers to a given positive integer.

    Parameters
    ----------
    num: int
        A positive integer.
    Returns
    -------
    list[int]
        A list of all the abundant numbers up to num.
    """
    res = []

    divisors = divisors_up_to(num)
    divisor_sums = {}
    for key in divisors:
        divisor_sums[key] = np.sum(divisors[key]) - key
    abundant_numbers = [key for key in divisor_sums if divisor_sums[key] > key]
    return abundant_numbers

def abundant_sums():
    """
    Returns a list of all numbers that can be written as the sum of two abundant numbers.
    
    Returns
    -------
    A list that contains all the numbers up to num that cannot be written as the sum of two abundant numbers.
    """
    abundants = abundant_numbers_up_to(28123)
    abundants.sort()
    sums = []
    for i in range(len(abundants)):
        for j in range(i,len(abundants)):
            if(abundants[i] + abundants[j] > 28123):
                break
            sums += [abundants[i] + abundants[j]]
    return list(set(sums))

sums = abundant_sums()
res = np.sum([x for x in range(1,28124)]) - np.sum(sums)
print(res)
