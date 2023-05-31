from functools import reduce

"""
sum_square_difference

Input: an integer N
Output: the values of (sum_{i=1}^N i)^2 - sum_{i=1}^N i^2
"""

def sum_square_difference(N):
    #the function counts each subset {a,b} twice,
    #so that we don't have to multiply the result by 2
    nums = range(1, N+1)
    return reduce(lambda x,y: x+y,[a*b for a in nums for b in nums if a!=b])

#a more efficient method
def sum_square_difference2(N):
    square_of_sums = reduce(lambda x,y: x+y, [i for i in range(1, N+1)])**2
    sum_of_squares = reduce(lambda x,y: x+y, [i**2 for i in range(1, N+1)])
    return square_of_sums - sum_of_squares
