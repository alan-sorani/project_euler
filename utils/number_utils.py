import numpy as np
import itertools
from numpy import floor,sqrt
from itertools import permutations, combinations
from functools import cache
from math import comb as binom

class IntsUpTo:
    """
    A class representing non-negative integers up to a given maximal integer.
    Contains number-theoretic methods that benefit from knowing an upper bound.
    
    Parameters
    ----------
    max_num : int
        A positive integer representing the maximum integer for the set of integers in the class.

    Attributes
    ----------
    max_num : int
    primes : list[int]
        A list of all the positive prime integers up to max_num, in increasing order.
    """

    def __init__(self, max_num : int):
        if(not isinstance(max_num, int)):
            raise ValueError("__init__ method for class IntsUpTo received a non-integer value.")
        if(max_num < 1):
            raise ValueError("__init__ method for class IntsUpTo received a non-positive integer.")
        self.max_num = max_num
        self.primes = sieve_of_eratosthenes(max_num) 

    @cache
    def sum_of_divisors(self, num : int) -> int:
        """
        Returns the sum of divisors of a non-negative integer.

        Parameters
        ----------
        num : int
            A non-negative integer.

        Returns
        -------
        int
            The sum of divisors of num.
        """
        if(num < 0):
            raise ValueError("Function sum_divisors of class IntsUpTo "
                             "received a negative value.")
        if(num in {0,1}):
            return num
        temp = num
        i = 0
        res = -1
        for prime in self.primes:
            if(prime**2 > temp):
                return temp + 1
            deg = 0
            while(temp % prime == 0):
                temp /= prime
                deg += 1
            if(deg > 0):
                res = np.sum([prime**i for i in range(deg+1)]) * self.sum_of_divisors(temp)
                break
        if(res == -1):
            raise ArithmeticError(f"Couldn't find a divisor of {num}.")
        if(res <= num):
            raise ArithmeticError(f"Calculated sum of divisors {res} for {num}, "
                                  "where the latter should be smaller.")
        return res
        
def polygonal_number(sides : int, n : int) -> int:
    """
    Computes a polygonal number.

    Parameters
    ----------
    sides : int
        The number of sides of the polygon.
    n : int
        The index for the polygonal number.

    Returns
    -------
    int
        The n'th polygonal number where the polygon is with the given number of sides.
    """
    return (sides - 2) * binom(n,2) + n

def get_polygonal_index(sides : int, n : int) -> tuple[int,bool]:
    """
    Returns the index of the smallest polygonal with the given number of sides that is at most as large as the given number,
    and True if the number itself is polygonal with that number of sides, or False otherwise.
    """
    if(sides == 2):
        n_sqrt = int(np.floor(np.sqrt(n)))
        is_polygonal = True
        if(n_sqrt ** 2 != n):
            is_polygonal = False
        return (n_sqrt, is_polygonal)
    temp = 8 * (sides - 2) * n + (sides - 4)**2
    temp_sqrt = int(np.floor(np.sqrt(temp)))
    is_polygonal = True
    if(temp_sqrt ** 2 != temp):
        is_polygonal = False
    numerator = temp_sqrt + (sides - 4)
    denominator = 2 * (sides - 2)
    if(numerator % denominator != 0):
        is_polygonal = False
    return (int(numerator / denominator), is_polygonal)

def different_digit_numbers():
    """
    Creates a generator for positive integers with different digits.
    """
    digit_strs = [str(d) for d in range(1,10)]
    num_digits = 1
    while(num_digits < 10):
        for comb in combinations(digit_strs, num_digits):
            for perm in permutations(comb):
                yield int(''.join(perm))
        num_digits += 1

def pandigitals(reverse : bool = False):
    """
    Creates a generator for pandigital numbers.
    """
    num_digits = 9 if reverse else 1
    while(num_digits > 1 if reverse else num_digits < 10):
        digits = ''.join([str(d) for d in range(1, num_digits + 1)])
        perms = list(permutations(digits))
        if(reverse):
            perms = perms[::-1]
        for perm in perms:
            yield int(''.join(perm))
        num_digits += (-1) if reverse else 1

def is_prime(n : int) -> bool:
    result = True
    i = 1
    while(result == True and i<floor(sqrt(n))):
        i+=1
        if(n/i == int(n/i)):
            result = False
    return result

def sieve_of_eratosthenes(num : int) -> list[int]:
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


def index_iterator(shape) -> itertools.product:
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

def increment_sequence(sequence: list[int], max_vals: list[int], skip = False) -> bool:
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

def factorize_up_to(num: int) -> dict[int,int]:
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

def factorization_to_divisors(factorization: list[tuple[int,int]]) -> list[int]:
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

def divisors_up_to(num: int) -> dict[int, list[int]]:
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
