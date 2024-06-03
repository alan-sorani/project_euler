# The way the spirals are formed, at distance d from the center, the numbers on the diagonal form an arithmetic sequence with step 2d. Furthermore, the first element at distance d is the last element at distance d-1, plus 2d.

import numpy as np

sum = 1
d = 1
first = 1
last = 1

while(d <= np.floor(1001/2)):
    first = last + 2 * d 
    last = first + 6 * d 
    sum += 4 * (first + last) / 2
    d += 1

print(sum)
