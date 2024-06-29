import numpy as np
from numpy import floor, sqrt

'''
We create a generator for the diagonal elements of the spiral.
'''

def diagonal_elements():
    level = 0
    value = 1
    corner_count = 4
    yield(value,level)
    while(True):
        corner_count += 1
        value += 2 * level
        if(corner_count == 5):
            corner_count = 1
            value += 2
            level += 1
        yield(value,level)

def is_prime(n):
    result = True
    i = 1
    while(result == True and i<floor(sqrt(n))):
        i+=1
        if(n/i == int(n/i)):
            result = False
    return result

if(__name__ == "__main__"):
    percentage = 100
    number_count = 0
    corner_count = 3
    prime_count = 0
    for diag in diagonal_elements():
        number_count += 1
        corner_count += 1
        if((corner_count != 4) and is_prime(diag[0])):
            prime_count += 1
            continue
        if(corner_count == 4):
            corner_count = 0
            percentage = 100 * prime_count / number_count 
            print(f"{diag[1]} --- {percentage}%")
            if(diag[1] != 0 and percentage < 10):
                break

    length = 2 * diag[1] + 1
    print(f"\n{length}")
