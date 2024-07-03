from math import factorial
from math import comb as binom
import numpy as np

if __name__ == "__main__":
    count = 0
    for n in range(1,101):
        for r in range(2, int(np.floor(n/2))+1):
            if(binom(n,r) > 10**6):
                count += 1
                count += (r * 2 != n)
    print(count)
