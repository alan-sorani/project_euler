import numpy as np

'''
Assume :math:`n = \sum_{i=0}^k d_i * 10^k` with :math:`d_k \neq 0` can be written as the sum of fifth powers of its digits. Then :math:`n = \sum_{i=0}^k d_i^5 \leq k * 9^5`. For k >= 6 the second expression is smaller than :math:`10^k`, so there cannot be equality.
Hence, we must only check numbers with up to 6 digits.
'''

power = 5
max_num = 999999
sum = 0

print("")

for num in range(2,max_num+1):
    digits = np.array(list(str(num)), dtype=int)
    if(num == np.sum([digit**power for digit in digits])):
        sum += num
        text = f"{num} = "
        for digit in digits:
            text += f"{digit}^{power} + "
        print(text[:-3])

print(f"\nsum = {sum}")
