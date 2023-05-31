from functools import reduce

"""
sum_square_difference

Input: an integer N
Output: the values of (sum_{i=1}^N i)^2 - sum_{i=1}^N i^2
"""

def sum_square_difference(N):
    #the function counts each subset {a,b} twice, so that we don't have to multiply the result by 2
    nums = range(1, N+1)
    return reduce(lambda x,y: x+y,[a*b for a in nums for b in nums if a!=b])
