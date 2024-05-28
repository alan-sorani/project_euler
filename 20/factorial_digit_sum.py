import numpy as np
num = np.math.factorial(100)
res = np.sum([int(x) for x in str(num)])
print(res)
