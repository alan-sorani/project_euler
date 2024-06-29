'''
Sadly this attempt to calculate the probabilities through linear algebra results in complex values for the probabilities.
I will keep this attempt here as I believe it could be used as a basis for a solution.
'''

import numpy as np
from sympy import Matrix, re, im
from itertools import product

import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from probability_utils import dice_sum_distribution

tiles = ["GO",
          "A1",
          "CC1",
          "A2",
          "T1",
          "R1",
          "B1",
          "CH1",
          "B2",
          "B3",
          "JAIL",
          "C1",
          "U1",
          "C2",
          "C3",
          "R2",
          "D1",
          "CC2",
          "D2",
          "D3",
          "FP",
          "E1",
          "CH2",
          "E2",
          "E3",
          "R3",
          "F1",
          "F2",
          "U2",
          "F3",
          "G2J",
          "G1",
          "G2",
          "CC3",
          "G3",
          "R4",
          "CH3",
          "H1",
          "T2",
          "H2"
    ]

if(__name__ == "__main__"):
    positions = dict([(value, key) for key, value in enumerate(tiles)])
    transition_probabilities = dict([(pair, 0) for pair in product(tiles,tiles)])

    dice_num = 2
    dice_sides = 6
    dice_max = dice_num * dice_sides
    dice_combinations = dice_sides ** dice_num
    dice_probabilities = dice_sum_distribution(dice_num, dice_sides)
    # the chance that all dice are equal, depending on the roll
    diagonal_probabilities = np.array([0 if roll % dice_num != 0 or dice_probabilities[roll] == 0 else 1 / (dice_combinations * dice_probabilities[roll]) for roll,prob in enumerate(dice_probabilities)])
    # the total chance that all the dice are equal
    p_diag = dice_sides / dice_combinations
    # the chance for jail, given a roll, as shown in the attached pdf
    jail_probabilities =  [((1 + 2 * p_diag**2 - np.sqrt(1 + 4 * p_diag**2)) * prob)/(2 * p_diag**2) for roll,prob in enumerate(diagonal_probabilities)]

    # calculate the probabilities of getting from one tile to another, ignoring any card draws or the effect of G2J
    for tile in tiles:
        for roll,probability in enumerate(dice_probabilities):
            target_tile = tiles[(positions[tile] + roll) % len(tiles)]
            transition_probabilities[(tile,target_tile)] += probability * (1 - jail_probabilities[roll])
            transition_probabilities[(tile,"JAIL")] += probability * jail_probabilities[roll]

    
    # move probabilities of ending at G2J to those ending at JAIL
    for tile in tiles:
        temp = transition_probabilities[(tile, "G2J")]
        transition_probabilities[(tile, "G2J")] = 0
        transition_probabilities[(tile, "JAIL")] += temp

    
    # consider cards in the Chance (CH) deck
    for i in range(1,4):
        ch = f"CH{i}"
        for tile in tiles:
            temp = transition_probabilities[(tile, ch)]
            transition_probabilities[(tile, ch)] = (6/16) * temp
            transition_probabilities[(tile, "GO")] += temp / 16
            transition_probabilities[(tile, "JAIL")] += temp / 16
            transition_probabilities[(tile, "C1")] += temp / 16
            transition_probabilities[(tile, "E3")] += temp / 16
            transition_probabilities[(tile, "H2")] += temp / 16
            transition_probabilities[(tile, "R1")] += temp / 16
            # consider the cards sending to the next railway company
            next_train = {1 : "R2", 2 : "R3", 3 : "R1"}
            transition_probabilities[(tile, next_train[i])] += (2/16) * temp
            # consider the cards sending to utility company
            if(i in {1,3}):
                transition_probabilities[(tile, "U1")] += temp / 16
            else:
                transition_probabilities[(tile, "U2")] ++ temp / 16
            # consider the cards sending the player 3 squares backwards
            end_tile = {1 : "T1", 2 : "D3", 3 : "CC3"}
            transition_probabilities[(tile, end_tile[i])] += temp / 16

    # consider cards in the Community Chest (CC) deck
    for i in range(1,4):
        cc = f"CC{i}"
        for tile in tiles:
            temp = transition_probabilities[(tile, cc)]
            transition_probabilities[(tile, cc)] = temp * (14/16)
            transition_probabilities[(tile,"JAIL")] += temp / 16
            transition_probabilities[(tile, "GO")] += temp / 16

    '''
    Having the transition probabilities between each pair of tiles, we create the transition matrix T for the system, where the (i,j) entry has the probability of moving from the i'th square to the j'th one.
    Using the law of total probability, if P[k] is the probability of being in tile k, we get that :math:`P[k] = \sum_{i=1}^{40} T[i,k] P[i]`, or equivalently that :math:`\sum_{i=1}^{40} (T - I)[i,k] P[i] = 0`. I.e. we have to find eigenvectors of the eigenvalue 1 of T.
    '''
    transition_matrix = np.array(
        [
            [
                transition_probabilities[tiles[j], tiles[i]]
                for i in range(40)
            ]
            for j in range(40)
        ]
    )

    # for rows that don't exactly sum to 1 due to calculation error, normalize them so that they sum to 1
    for row in range(40):
        transition_matrix[row] *= 1/np.sum(transition_matrix[row])

    transition_matrix = Matrix(transition_matrix)
    is_one = lambda val: np.isclose(float(re(val)), 1) and np.isclose(float(im(val)),0)
    eigenvects = Matrix(transition_matrix.transpose()).eigenvects()
    eigenvects = [vects[2] for vects in eigenvects if is_one(vects[0])]
    print(eigenvects)
