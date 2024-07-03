from sympy import Matrix
from time import time

'''
We use our function for counting triplets from the solution for problem 75.
'''

A = Matrix([[1,-2,2],[2,-1,2],[2,-2,3]])
B = Matrix([[1,2,2],[2,1,2],[2,2,3]])
C = Matrix([[-1,2,2],[-2,1,2],[-2,2,3]])

def perimeter(triplet):
    return triplet[0] + triplet[1] + triplet[2]

def increase_count(dictionary, key):
    if(key in dictionary):
        dictionary[key] += 1
    else:
        dictionary[key] = 1

def count_triplets(triplet, perimeter_counts, max_perimeter):
    this_perimeter = perimeter(triplet)
    if (this_perimeter > max_perimeter):
        return 0
    temp = this_perimeter
    while(temp < max_perimeter):
        increase_count(perimeter_counts, temp)
        temp += this_perimeter
    count_triplets(A @ triplet, perimeter_counts, max_perimeter)
    count_triplets(B @ triplet, perimeter_counts, max_perimeter)
    count_triplets(C @ triplet, perimeter_counts, max_perimeter)

def solution(max_perimeter = 1000):
    perimeter_counts = {}
    triplet_0 = Matrix([3,4,5])
    count_triplets(triplet_0, perimeter_counts, max_perimeter)
    return max(perimeter_counts, key=perimeter_counts.get)

if(__name__ == "__main__"):
   start = time()
   print(solution())
   end = time()
   diff = end - start
   print(f"Solution found in {diff} seconds.")
