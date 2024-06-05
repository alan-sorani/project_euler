import numpy as np

# We first load the data and put it in a numpy array.

with open("matrix.txt", "r") as file:
    text = file.read()
text = text.split("\n")
text = [line.split(",") for line in text[:-1]]
matrix = np.array(text)
matrix = matrix.astype(int)
rows, cols = matrix.shape

# We use the same method as in problems 18 and 67, since the only difference is that there are non-zero elements below the secondary diagonal, and that we need to minimize the sum instead of maximizing it.

# for the last row/column, add each number to those to its left/up respectively
for i in range(cols - 2, -1, -1):
    matrix[rows - 1, i] += matrix[rows - 1, i + 1]
for i in range(rows - 2, -1, -1):
    matrix[i, cols - 1] += matrix[i + 1, cols - 1]

# for the rest of the entries, add the minimum between the numbers below and to its right to itself, in decreasing lexicographical order on the indices
for i in range(rows - 2, -1, -1):
    for j in range(cols - 2, -1, -1):
        matrix[i,j] += np.min([matrix[i+1,j], matrix[i,j+1]])

# print the result
print(matrix[0,0])
