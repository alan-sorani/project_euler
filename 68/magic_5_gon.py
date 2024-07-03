from itertools import combinations, permutations
import numpy as np

'''
We notice that if the different rows of numbers are arranged as the rows of a matrix A, then they solve the magic 5-gon if and only if we have that A[0,0] = max_j(A[0,j]), that the sums of the rows are equal and that A[i,2] = a[(i+1)%5,1] for all i. 
'''

def test_magic_5_gon(entries : np.ndarray):
    if(entries[0,0] != np.min(entries[:,0])):
        return False
    first_row_sum = np.sum(entries[0,:])
    for i in range(entries.shape[0]):
        if(np.sum(entries[i,:]) != first_row_sum):
            return False
        if(entries[i,2] != entries[(i+1)%5, 1]):
           return False
    return True

def list_to_5_gon(nums : list[int]):
    res = np.zeros(shape = (5,3), dtype=int)
    res[:,:2] = np.reshape(nums, (5,2), order='F')
    for i in range(5):
        res[i, 2] = res[(i+1) % 5, 1]
    return res

def concatenate_numbers(nums: list[int]):
    return int(''.join([str(num) for num in nums]))

if __name__ == "__main__":
    res = 0
    for perm in permutations([i for i in range(1,11)]):
        if(10 not in perm[:5]):
            continue
        five_gon = list_to_5_gon(perm)
        if(test_magic_5_gon(five_gon)):
            number_string = concatenate_numbers(np.reshape(five_gon, (15,)))
            if(number_string > res):
                res = number_string
    print(res)
