import numpy as np

'''
Numbers from 10^{k-1} to 10^{k} - 1 have k digits in their decimal representation.
There are 10^{k} - 10^{k-1} = 10^{k-1} * (10 - 1) = 9 * 10^{k-1} such numbers, which then have 9 * 10^{k-1} * k digits total.
To find the n'th digit, we first find how many digits the number its contained in has, and then find the correct digit within those numbers.
'''

num_digits_in_length = [9 * 10**(k-1) * k for k in range(20)]
num_digits_up_to_length = [int(np.sum(num_digits_in_length[:k])) for k in range(20)]

def find_digit(digit_index : int):
    length_of_num = 0
    for i, num_digits in enumerate(num_digits_up_to_length):
        if (num_digits >= digit_index):
            length_of_num = i - 1
            break
    # the index of the digit to be searched when starting to count only from numbers of the specific length
    digit_in_length = digit_index - num_digits_up_to_length[length_of_num]
    # the index of the number within numbers of that length, in which the digit appears
    relative_num_of_digit = int(np.ceil(digit_in_length / length_of_num))
    num_of_digit = relative_num_of_digit + 10**(length_of_num - 1) - 1
    index_in_num = digit_in_length - length_of_num * (relative_num_of_digit - 1)
    return int(str(num_of_digit)[index_in_num-1])

if(__name__ == "__main__"):
    res = 1
    for i in range(7):
        res *= find_digit(10**i)
    print(res)
