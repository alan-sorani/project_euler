import numpy as np

character_value = {}
for order in range(ord('A'), ord('Z') + 1):
    character_value[chr(order)] = order - ord('A') + 1

def word_value(word : str):
    return int(np.sum([character_value[char] for char in word]))

def is_triangle(num : int):
    """
    Checks whether a given positive integer is triangle.

    Parameters
    ----------
    num : int
        A positive integer.

    Returns
    -------
    True if num is a triangle number, or False otherwise.

    Notes
    -----
    A triangle number is of the form :math:`t_n \coloneqq n(n+1)/2` for a positive integer n. Expressing n from this equation we get that it equals :math:`\frac{-1 \pm \sqrt(1 + 8 t_n)}{2}, so a number m is a triangle number if and only if 1 + 8m is a square.
    """
    temp = 1 + 8 * num
    return np.round(np.sqrt(temp)) ** 2 == temp

if __name__ == "__main__":
    with open("words.txt", "r") as file:
        input = file.read()
        words = input.split(',')
        words = [word[1:-1] for word in words]
        triangle_words = [is_triangle(word_value(word)) for word in words]
        print(triangle_words.count(True))
