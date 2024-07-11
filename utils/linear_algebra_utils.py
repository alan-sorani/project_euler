import numpy as np
from sympy import Matrix

def inner_product(u : Matrix(n,1), v : Matrix(n,1)):
    return (u.transpose()@v)[0]

if __name__ == "__main__":
