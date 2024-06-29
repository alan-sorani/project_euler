import numpy as np
from numpy.random import randint

def dice_roll(dice_num : int, dice_sides : int):
    """
        Returns a random roll of dice.

        Parameters
        ----------
        dice_num : int
            The number of dice to be rolled.
        dice_sides : int
            The number of sides for each dice, numbered 1 through dice_sides.

        Returns
        -------
        list[int]
            A list containing a random dice roll, where each dice is uniformly distributed.
    """
    return randint(1,dice_sides + 1, size=dice_num)
def dice_sum(dice_num : int, dice_sides : int):
    """
        Returns the sum of a random roll of dice.

        Parameters
        ----------
        dice_num : int
            The number of dice to be rolled.
        dice_sides : int
            The number of sides for each dice, numbered 1 through dice_sides.

        Returns
        -------
        int
            The sum of a random dice roll, where each dice is uniformly distributed.
    """
    return np.sum(dice_roll(dice_num, dice_sides))
