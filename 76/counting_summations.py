from math import comb as binom

def count_summations_k(num : int, k : int):
    '''
    Counts the number of ways of writing num as the sum of k integers.
    We do these by looking at num balls in a row, and seeing that splitting them into k groups of size at least 1 is the same as adding k-1 balls and choosing which of the num-2 inner balls act as separators.
    '''
    return binom(num+k-3, k-1)

def count_summations(num : int):
    '''
    Counts the number of ways of writing a given number as the sum of more than one integer.
    '''
    res = 0
    for k in range(2,num+1):
        res += count_summations_k(num, k)
    return res

if(__name__ == "__main__"):
    print(count_summations_k(5,2))
