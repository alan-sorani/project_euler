import numpy as np

def collatz_sequence(first_number: int):
    """
    Returns the Collatz sequence starting with a given number.

    Parameters
    ----------
    first_number: int
        The first number of the Collatz sequence to be returned.
    Returns
    -------
    list[int]
        The Collatz sequence starting at the number first_number.
    """
    res = [first_number]
    current_number = first_number
    while(current_number != 1):
        if(current_number % 2 == 0):
            current_number = current_number / 2
        else:
            current_number = 3 * current_number + 1
        res += [current_number]
    return res

def longest_collatz_sequence(max_number: int):
    """
    Returns the starting number that produces the longest Collatz sequence, and the matching sequence, where the starting number is bounded from above by max_number.
    
    Parameters
    ----------
    max_number: int
        The maximal number to be checked for starting the longest sequence.
    Returns
    -------
    tuple[int, list[int]]
        A tuple where the first integer is the starting number that produces the longest Collatz sequence, from those sequences where the starting number is up to max_number, and where the list is that longest sequence.
    """
    res_number = 1
    res_sequence = [1]
    starting_numbers = [i for i in range(max_number+1)]
    for starting_number in starting_numbers[2:]:
        if(starting_number != 0):
            sequence = collatz_sequence(starting_number)
            for n in sequence:
                if(n <= max_number):
                    starting_numbers[int(n)] = 0
            if(len(sequence) > len(res_sequence)):
                res_number = starting_number
                res_sequence = sequence
    return (res_number, res_sequence)
