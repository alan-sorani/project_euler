import numpy as np
from math import factorial

'''
Assume :math:`n = \sum_{i=0}^k d_i * 10^k` with :math:`d_k \neq 0` can be written as the sum of the factorials of its digits. Then :math:`n = \sum_{i=0}^k d_i! \leq k * 9!`.
We have 9! = 362880, so :math:`n \leq k * 362880`. This isn't possible for k >= 7, so we get that n has at most 7 digits.
Hence, we must only check numbers with up to 6 digits.
'''

max_num = 10**7
sum = 0

print("")

for num in range(2,max_num):
    digits = np.array(list(str(num)), dtype=int)
    if(num == np.sum([factorial(digit) for digit in digits])):
        sum += num
        text = f"{num} = "
        for digit in digits:
            text += f"{digit}! + "
        print(text[:-3])

print(f"\nsum = {sum}")
