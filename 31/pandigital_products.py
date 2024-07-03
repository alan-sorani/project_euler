import numpy as np
from itertools import permutations, combinations

'''
We note that the product of two numbers with 4 digits between them is less than 10**4 = 10000 and therefore has at most 4 digits.
Hence, if m * n = l is a pandigital product, the number of digits between m,n has to be at least 5.
It cannot be more than 5, because l cannot have the correct number of digits. Assuming n has at least the number of digits that m has:
    - If m has 1 digit, n would have at least 5, so l has to have more than 3 digits.
    - If m has 2 digits, n would have at least 4, so again l has to have more than 3 digits.
    - If m has 3 digits, n would have at least 3 digits. But then m*n >= 100**2 = 10000, so l must have at least 5 digits.

We get that m,n should together have 5 diigts and that l has 4 digits.
'''

def test_product(num : int):
    """
    Takes a 4-digit positive integer and check if it can be written as the product of two integers such that each digit appears exactly once amongs the three integers.
    """
    digits = list(str(num))
    other_digits = [i for i in "123456789" if i not in digits]
    for perm in permutations(other_digits):
        for i in range(1,5):
            m,n = int(''.join(perm[:i])), int(''.join(perm[i:]))
            if(m * n == num):
                return True
    return False

def pandigital_products():
    digits = "123456789"
    four_digit_choices = [comb for comb in combinations(digits,4)]
    nums_to_test = [[perm for perm in permutations(digit_choice)] for digit_choice in four_digit_choices]
    nums_to_test = [
                    num
                    for combination in nums_to_test
                    for num in combination
    ]
    nums_to_test = [int(''.join(num)) for num in nums_to_test]
    
    return np.sum([num for num in nums_to_test if test_product(num)])

if __name__ == "__main__":
    print(pandigital_products())
    
