import numpy as np

'''
The problem is easy enough that we can brute-force through it.
'''

max_num = 100
res = []

for a in range(2,max_num+1):
    for b in range(2,max_num+1):
        res += [a**b]

print(len(set(res)))
