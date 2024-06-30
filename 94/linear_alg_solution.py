from sympy import Matrix
from time import time

def solution():

    A = Matrix([[1,-2,2],[2,-1,2],[2,-2,3]])
    C = Matrix([[-1,2,2],[-2,1,2],[-2,2,3]])

    def pythagorean_to_lengths(triplet : Matrix, triplet_type : str):
        h = triplet[1] if (triplet_type[1] == "1") else triplet[0]
        m = triplet[0] if (triplet_type[1] == "1") else triplet[1]
        a = 2 * m - 1 + 2 * (triplet_type[0] == "U")
        b = 2 * m
        return(a,b)

    def perimeter(lengths : Matrix):
        return 2 * lengths[0] + lengths[1]

    triplet_0 = Matrix([3,4,5])
    res = 0
    triplet_type = "L1"
    triplet = triplet_0
    triplet_perimeter = perimeter(pythagorean_to_lengths(triplet, triplet_type))
    max_perimeter = 10**9

    while(triplet_perimeter < max_perimeter):
        lengths = pythagorean_to_lengths(triplet, triplet_type)

        res += perimeter(lengths)
        triplet = C @ triplet if (triplet_type == "L1") else A @ triplet
        triplet_type = "U2" if (triplet_type == "L1") else "L1"
        triplet_perimeter = perimeter(pythagorean_to_lengths(triplet, triplet_type))

    return res

if(__name__ == "__main__"):
   start = time()
   print(f"Solution = {solution()}")
   end = time()
   diff = end - start
   print(f"Solution found in {diff} seconds.")
