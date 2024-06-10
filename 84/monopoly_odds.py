import numpy as np
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
    # the chance for jail, given a roll, is the chance to roll a double times the chance that the previous two rolls were exactly the same
    jail_probabilities =  diagonal_probabilities / dice_combinations**2
    print(dict(enumerate(diagonal_probabilities)))

    for tile in tiles:
        for roll,probability in enumerate(dice_probabilities):
            target_tile = tiles[(positions[tile] + roll) % len(tiles)]
            transition_probabilities[(tile,target_tile)] += probability

    
