import numpy as np
from math import inf

'''
An h x w rectangle fits in an m x n grid (m-h+1)*(n-w+1) times. Hence the number of rectangles is the sum of this value over all values of h between 1 and m and over all values of w between 1 and n. Separating the sum and using the sum of an arithmetic sequence, we get that the number of rectangles is (m*(m+1)*n*(n+1))/4. Hence we need m*(m+1)*n*(n+1) to be the closest to 8 million.
'''

best_error = inf
prev_error = inf
approx = [0,0]

for m in range(1, int(np.sqrt(8000000)+1)):
    prev_error = inf
    for n in range(1, int(np.sqrt(8000000)+1)):
        error = np.abs(8000000 -m*(m+1)*n*(n+1))
        print(f"m = {m}, n = {n}, m*(m+1)*n*(n+1) = {m*(m+1)*n*(n+1)}, error={error}")
        if(error > prev_error):
            break
        if(error < best_error):
            best_error = error
            approx = [m,n]
        prev_error = error
print (approx, best_error)
