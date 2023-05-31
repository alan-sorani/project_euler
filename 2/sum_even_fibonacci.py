from numpy import sqrt

phi = (1 + sqrt(5))/2
psi = (1 - sqrt(5))/2

"""
fibonacci

Input: an integer n
Output: the nth Fibonacci number
"""

def fibonacci(n):
    return round((phi**n - psi**n)/sqrt(5))

"""
sum_even_fibonacci

Input: an integer max_num

Output: the sum of all even Fibonacci numbers that do not exceed max_num

Proof:

1. Even Fibonacci numbers are every number whose index is 2 (mod 3):
    mod 2, the first two numbers are 0,1 so the sequence becomes
    0,1,1,0,1,1,0,1,1,0,...
2. The even numbers are given where we have 0, which is when the index is
    0 (mod 3)


"""
def sum_even_fibonacci(max_num):
    result = 0
    i = 0
    fibonacci_number = fibonacci(i)
    while(fibonacci_number <= max_num):
        result += fibonacci_number
        i+=3
        fibonacci_number = fibonacci(i)
    return result
