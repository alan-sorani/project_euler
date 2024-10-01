import numpy as np
from sympy import Matrix
from numpy import arccos

def inner_product(u : Matrix(n,1), v : Matrix(n,1)) -> float:
    return (u.transpose()@v)[0]

def norm(u : Matrix(n,1)) -> float:
    return np.sqrt(inner_product(u,u))

def angle(u : matrix(n,1), v : Matrix(n,1)):
    return arccos(inner_product(u,v) / (norm(u) * norm(v)))

if __name__ == "__main__":
