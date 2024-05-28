import numpy as np

# we use brute-force to calculate the power and sum its digits

sum = np.sum([digit for digit in str(2**1000)])
print(sum)
