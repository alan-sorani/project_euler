import numpy as np

# the golden ratio
phi = (1 + 5**0.5)/2
log_phi = lambda x: np.log(x) / np.log(phi)

# indices above this give Fibonacci numbers above 10^999, based on the formula F_n = round(phi**n / sqrt(5))
print(log_phi(5**0.5) + 999*log_phi(10))
