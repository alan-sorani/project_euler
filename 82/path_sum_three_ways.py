import numpy as np
from math import inf

# We first load the data and put it in a numpy array.

with open("matrix.txt", "r") as file:
    text = file.read()
text = text.split("\n")
text = [line.split(",") for line in text[:-1]]
matrix = np.array(text)
matrix = matrix.astype(int)
rows, cols = matrix.shape

'''
We separate the problem by columns, considering the base case of two columns. In this case, for each element of the second column, we check the minimal sum of a path from each of the elements in the first column, using our solution for problem 81.

We do this starting from the right-most two columns and set the minimal sums in the respective entries of the first of the two columns. We repeat this until we set new values in the first column, and then take the minimum of these values.
'''

def min_path_to_corner(matrix):
    """
    Replaces each entry in the matrix with the minimal sum of numbers along a path from that entry to the bottom-right corner, where steps can go either right or down.
    
    Parameters
    ----------
    matrix: ndarray[int]
        A 2D numpy array containing non-negative integers.
    """
    rows, cols = matrix.shape

    # for the last row/column, add each number to those to its left/up respectively
    for i in range(cols - 2, -1, -1):
        matrix[rows - 1, i] += matrix[rows - 1, i + 1]
    for i in range(rows - 2, -1, -1):
        matrix[i, cols - 1] += matrix[i + 1, cols - 1]

    # for the rest of the entries, add the minimum between the numbers below and to its right to itself, in decreasing lexicographical order on the indices
    for i in range(rows - 2, -1, -1):
        for j in range(cols - 2, -1, -1):
            matrix[i,j] += np.min([matrix[i+1,j], matrix[i,j+1]])

for j in range(cols-2, -1, -1):
    min_paths = np.array([inf for i in range(rows)])
    for i in range(0, rows):
        upper_matrix = matrix[:i+1, j:j+2].copy()
        lower_matrix = matrix[i:, j:j+2].copy()
        lower_matrix = lower_matrix[::-1]
        min_path_to_corner(upper_matrix)
        min_path_to_corner(lower_matrix)
        lower_matrix = lower_matrix[::-1]
        min_paths[:i+1] = np.minimum(min_paths[:i+1], upper_matrix[:,0])
        min_paths[i:] = np.minimum(min_paths[i:], lower_matrix[:,0])
    matrix[:,j] = min_paths

print(np.min(matrix[:,0]))
        
