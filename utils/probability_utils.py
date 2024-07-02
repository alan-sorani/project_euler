import numpy as np
from math import comb as binom

def dice_sum_distribution(dice_num : int, dice_sides : int):
    """
        Returns a list containing the probability distribution for the sum of rolling a given number of n-sided dice.

        Parameters
        ----------
        dice_num : int
            The number of dice to be rolled.
        dice_sides : int
            The number of sides for each dice, numbered 1 through dice_sides.

        Returns
        -------
        list[int]
            A list indexed by 0 through dice_num*dice_sides where at each index is the probability that the sum of the dice values will be equal that index.

        Notes
        -----
        Assume we want to count the number of ways the dice sum to n. This is exactly the number of ways that dice numbered 0 through dice_sides-1 sum to n-dice_num, so we may reduce the calculation to the case of dice numbered in the latter manner.
        The number of ways to write n as a sum of d non-negative integers is equal to the number of ways of arranging n balls in k distinct bins. This equals :math:`\binomial{n + d - 1}{d - 1}` as can be shown by choosing separators between the balls.
        The number of ways to distribute n balls so that at least i of the k bins have more than d balls is then
        .. math::
            \binomial{k}{i} \binomial{n+k-1-i(d+1)}{k-1}
        up to counting each combination multiple times if there are more than i bins with more than d balls in them.
        Therefore, the number of ways to distribute n balls in k bins such that none of the bins has more than d balls is exactly
        .. math::
            N(n, k, d) \coloneqq \sum_{i=0}^{\floor{\frac{n}{d+1}}} (-1)^i \binomial{k}{i}\binomial{n+k-1-i(d+1)}{k-1} \text{.}
        This equals the number of ways to get n as the sum of k dice with sides 0 through d. Hence the number of ways to get n as the sum of k dice with sides 1 through d is :math:`N(n-k, k, d-1)`.
    """
    max_sum = dice_sides * dice_num
    dice_combinations = dice_sides ** dice_num
    max_full_bins = lambda n,d : int(np.floor(n/(d+1)))+1
    summand = lambda n,k,d,i : 0 if i<0 else (-1)**i * binom(k,i) * binom(n+k-1-i*(d+1), k-1)
    N = lambda n,k,d: np.sum([summand(n,k,d,i) for i in range(max_full_bins(n,d))])
    res = np.array([N(i-dice_num, dice_num, dice_sides-1) for i in range(max_sum+1)]) / dice_combinations
    return res

if __name__ == "__main__":
    print("\n")
    print("Dice distribution for 2d6 is:")
    print(dict(enumerate(dice_sum_distribution(2,4))))
