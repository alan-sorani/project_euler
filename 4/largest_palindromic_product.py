"""
is_palindrome

Input: an integer num
Output: True if num is a palindrome and False otherwise
"""
def is_palindrome(num):
    string = str(num)
    length = len(string)
    for i in range(int(length/2)):
        if (string[i] != string[length-i-1]):
            return False
    return True

"""
largest_palindromic_product

Input: an integer num_digits
Output: the largest palindrome made from the product of two numbers which have num_digits digits each
"""
def largest_palindromic_product(num_digits):
    factors = [n for n in range(10**(num_digits-1), 10**(num_digits))]
    numbers = [n*m for n in factors for m in factors if is_palindrome(n*m)]
    return max(numbers)

"""
improved_lpp

a more efficient version of the above function in the case where num_digits = 3
"""

def improved_lpp_3():
    largest_palindrome = 0
    a = 999
    while(a >= 100):
        b = 999
        if (a%11 == 0):
            db = 1
        else:
            db = 11
        while(b >= a):
            if a*b <= largest_palindrome:
                break
            if is_palindrome(a*b):
                largest_palindrome = a*b
            b-=db
        a-=1
    return largest_palindrome
