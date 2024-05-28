import numpy as np
import itertools

def index_list(shape):
    """
    Returns a list of indices for an array of the given shape.

    Parameters
    ----------
    shape: tuple[int, ..., int]
        The shape of an array.
    Returns
    -------
    list[tuple[int]]
        A list containing the indices of an array of the given shape.
    """
    ranges = [range(dim) for dim in shape]
    product = itertools.product(*ranges)
    indices = list(product)
    return indices

def previous_indices(index):
    """
    Returns a list of the previous indices of a given array index.

    Paremters
    ---------
    index: tuple[int, ..., int]
        A given index for an array.
    Returns
    -------
    tuple[int, ..., int]
        A list of all the indices of the form (i_1, ..., i_{k-1},  i_k - 1, i_{k+1} ..., i_n) where index = (i_1, ..., i_n). 
    """
    dims = len(index)
    res = []
    for dim in range(dims):
        if(index[dim] != 0):
            prev_index = index - np.eye(1,dims,dim,dtype=int)[0]
            res += [tuple(prev_index)]
    return res

def lattice_paths(shape):
    """
    Returns the number of ways to get to the bottom-right from the top-left of a square grid of a given shape.

    Parameters
    ----------
    shape: tuple[int, ..., int]
        The shape of a given square grid.
    Returns
    -------
    tuple[int, ndarray[int]]
        The number of ways to get to the bottom-right from the top-left of a square grid of the given shape.
    """
    grid = np.zeros(shape)
    dims = len(shape)
    indices = index_list(shape)
    grid[indices[0]] = 1
    for index in index_list(shape)[1:]:
        prev_indices = previous_indices(index) 
        prev_values = [grid[prev_index] for prev_index in prev_indices]
        grid[index] = np.sum(prev_values)
    return (grid[index], grid)
