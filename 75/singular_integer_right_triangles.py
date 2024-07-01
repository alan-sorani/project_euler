from sympy import Matrix
from time import time

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

def solution(max_perimeter = 1_500_000):
    perimeter_counts = {}
    triplet_0 = Matrix([3,4,5])
    count_triplets(triplet_0, perimeter_counts, max_perimeter)
    unique_perimeters = [key for key,value in perimeter_counts.items() if value == 1]
    return len(unique_perimeters)

if(__name__ == "__main__"):
   start = time()
   print(solution())
   end = time()
   diff = end - start
   print(f"Solution found in {diff} seconds.")
