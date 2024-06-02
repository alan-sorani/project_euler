import numpy as np

factorial = lambda x : np.math.factorial(x)

k = 1000000
available_digits = [0,1,2,3,4,5,6,7,8,9]
m = 9
res = []

for i in range(10):
    digit_index = int(np.ceil(k / factorial(m)))
    res += [available_digits.pop(digit_index - 1)]
    k -= (np.ceil(k/factorial(m)) - 1) * factorial(m)
    m -= 1
print(res)
