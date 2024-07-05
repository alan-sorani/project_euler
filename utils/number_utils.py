import numpy as np
import itertools
from numpy import floor,sqrt
from itertools import permutations

def pandigitals(reverse : False):
    """
    Creates a generator for pandigital numbers.
    """
    num_digits = 9 if reverse else 1
    while(num_digits > 1):
        digits = ''.join([str(d) for d in range(1, num_digits + 1)])
        perms = list(permutations(digits))
        if(reverse):
            perms = perms[::-1]
        for perm in perms:
            yield int(''.join(perm))
        num_digits += (-1) if reverse else 1

def is_prime(n : int):
    result = True
    i = 1
    while(result == True and i<floor(sqrt(n))):
        i+=1
        if(n/i == int(n/i)):
            result = False
    return result

def sieve_of_eratosthenes(num : int):
    """
    Returns a list containing all the integers up to a given number. 

    Parameters
    ----------
    num : int
        An integer.

    Returns
    -------
    list[int]
        A list of all the primes up to num.
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
    A dictionary where the keys are the positive integers up to num, and the values are their prime factorizations, as a list [(p_1, k_1), ..., (p_m, k_m)] where the number is the product of p_i^{k_i}.
    """
    primes = sieve_of_eratosthenes(num)
    num_primes = len(primes)
    res = dict([(x,[]) for x in range(1, num+1)])

    for prime in primes:
        # orders of divisibility for the specific prime
        prime_orders = dict([(x, 0) for x in range(1, num+1)])
        i = 1
        product = prime
        while(product <= num):
            order = prime_orders[i] + 1
            prime_orders[product] = order 
            res[product] += [(prime, order)]
            i += 1
            product = prime * i
    
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

def amicable_numbers_up_to(num: int):
    """
    Returns a list of all the amicable numbers to a given positive integer.

    Parameters
    ----------
    num: int
        A positive integer.
    Returns
    -------
    list[int]
        A list of all the amicable numbers up to num.
    """
    res = []

    divisors = divisors_up_to(num)
    divisor_sums = {}
    for key in divisors:
        divisor_sums[key] = np.sum(divisors[key]) - key
    max_divisor_sum = np.max([value for key,value in divisor_sums.items()])

    divisors = divisors_up_to(max_divisor_sum)
    divisor_sums = {}
    for key in divisors:
        divisor_sums[key] = np.sum(divisors[key]) - key
    
    for key,value in divisor_sums.items():
        if(key == 1 or key == value or value > max_divisor_sum):
            continue
        if(divisor_sums[value] == key):
            res += [key, value]

    res = [value for value in res if value <= num]
    
    return list(set(res))

if(__name__ == "__main__"):
    prime_factorizations = str(factorize_up_to(10**5))
    with open("prime_factorizations_1000000.txt","w") as file:
        file.write(prime_factorizations)
