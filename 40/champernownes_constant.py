import numpy as np

'''
Numbers from 10^{k-1} to 10^{k} - 1 have k digits in their decimal representation.
There are 10^{k} - 10^{k-1} = 10^{k-1} * (10 - 1) = 9 * 10^{k-1} such numbers, which then have 9 * 10^{k-1} * k digits total.
To find the n'th digit, we first find how many digits the number its contained in has, and then find the correct digit within those numbers.
'''

num_digits_in_length = [9 * 10**(k-1) * k for k in range(20)]
num_digits_up_to_length = [np.sum(num_digits_in_length[:k]) for k in range(20)]

def find_digit(digit_index : int):
    length_of_num = 0
    for i, num_digits in enumerate(num_digits_up_to_length):
        if (num_digits > digit_index):
            length_of_num = i - 1
            num_in_length = np.floor((digit_index - num_digits) / i)
            break
    num_of_digit = num_in_length + 10**(length_of_num - 1)
    return num_of_digit

if(__name__ == "__main__"):
    print(find_digit(100))
    
