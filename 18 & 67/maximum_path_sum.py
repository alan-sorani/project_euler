import numpy as np

def text_to_lines(text):
    """
    Takes a triangle of integers and places it in a list of lists, where each of the inner lists has the numbers on the corresponding level.
    
    Parameters
    ----------
    text: str
        A text representation of a triangle of numbers.
    Returns
    -------
    list[list[int]]
        A list of lists of integers, such that the i'th list has the integers of depth i of the triangle, where depth starts at 1.        
    """
    lines = text.split("\n")
    lines = [line.split(" ") for line in lines][:-1]
    
    for line in lines:
        for index, entry in enumerate(line):
            line[index] = int(entry)
    
    return lines

def lines_to_array(lines):
    """
    Takes the lines of a triangle as given by the output of text_to_lines, and returns an ndarray where each diagonal (i,j) such that i+j=k is fixed, has the entries of the k'th line of the input.
    Parameters
    ----------
    lines: list[list[int]]
        A list of the elements of a triangle of integers, where the k'th inner list is of the elements of depth k.
    Returns
    -------
    ndarray
        An ndarray where each diagonal (i,j) such that i+j=k has the entries of the k'th line of the input. The last level of the input is placed on the secondary diagonal of the array, and below it are zeros.
    """
    n = len(lines[-1])
    shape = (n,n)
    arr = np.zeros(shape)
    for k, line in enumerate(lines):
        for i, num in enumerate(line):
            arr[k-i, i] = num
    return arr

def arr_path_sums(arr):
    """
    Takes an ndarray as given by lines_to_array and outputs the maximum sum of the numbers through a path in the triangle, where a path is given by increasing one of the indices at each step.
    
    Parameters
    ----------
    arr: ndarray
        A 2D ndarray of integers where there are zeros below the secondary diagonal.
    Returns
    -------
    int
        The maximum sum of the integers in a path, where paths are given by increasing one of the indices by 1 at each step.
    """
    k = len(arr) - 2
    while(k >= 0):
        for i in range(k+1):
            arr[k-i, i] += np.max([arr[k-i+1,i], arr[k-i,i+1]])
        k = k - 1

def file_to_max_path_sum(file_name):
    """
    Takes a file name where the file has a text representation of a triangle of integers, and returns the maximum sum of integers across different paths in the triangle.
    """
    input = open(file_name)
    input = input.read()
    lines = text_to_lines(input)
    arr = lines_to_array(lines)
    arr_path_sums(arr)
    return arr[0,0]
