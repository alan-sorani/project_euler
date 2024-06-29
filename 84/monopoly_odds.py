import numpy as np
from sympy import Matrix, re, im
from itertools import product
from random import shuffle

import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
utils_path = "/".join(dir_path.split("/")[:-1] + ['utils'])
sys.path.append(utils_path)
from dice_utils import dice_roll

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
    
community_chest = [0 for i in range(14)] + ["GO"] + ["JAIL"]
chance_deck = [0 for i in range(6)] + ["JAIL", "C1", "E3", "H2", "R1", "R", "R", "U", -3]

'''
We simulate the game and count steps on each tile.
'''

if(__name__ == "__main__"):
    positions = dict([(value, key) for key, value in enumerate(tiles)])
    dice_num = 2
    dice_sides = 4
    player_tile = "GO"
    visits = dict([(tile, 0) for tile in tiles])
    double_count = 0
    chest_cards = community_chest.copy()
    shuffle(chest_cards)
    chance_cards = chance_deck.copy()
    shuffle(chance_cards)

    steps = 10000000
    for i in range(steps):
        visits[player_tile] += 1
        roll = dice_roll(dice_num, dice_sides)
        if(roll[0] == roll[1]):
            double_count += 1
        else:
            double_count = 0
        if(double_count == 3):
                double_count = 0
                player_tile = "JAIL"
        else:
            player_tile = tiles[(positions[player_tile] + np.sum(roll)) % 40]
            if(player_tile[:2] == "CH"):
                card_draw = chance_cards.pop()
                if(card_draw in {"JAIL", "C1", "E3", "H2", "R1"}):
                    player_tile = card_draw
                elif(card_draw == -3):
                    player_tile = tiles[(positions[player_tile] - 3) % 40]
                elif(card_draw == "R"):
                    if(player_tile[2] == "1"):
                        player_tile = "R2"
                    elif(player_tile[2] == "2"):
                        player_tile = "R3"
                    else:
                        player_tile = "R1"
                elif(card_draw == "U"):
                    if(player_tile[2] in {"1", "3"}):
                        player_tile = "U1"
                    else:
                        player_tile = "U2"
                if(len(chance_cards) == 0):
                    chance_cards = chance_deck.copy()
                    shuffle(chance_cards)
            if(player_tile[:2] == "CC"):
                card_draw = chest_cards.pop()
                if(card_draw != 0):
                    player_tile = card_draw
                if(len(chest_cards) == 0):
                    chest_cards = community_chest.copy()
                    shuffle(chest_cards)
            if(player_tile == "G2J"):
                player_tile = "JAIL"

visit_counts = [(key,item) for key,item in visits.items()]
visit_counts.sort(key = lambda a: a[1])
visit_counts = visit_counts[::-1]
visit_percentages = [(tile, 100 * count/steps) for tile,count in visit_counts]
print(f"The approximate percentages of landing on each tile when rolling {dice_num}d{dice_sides} and after {steps} steps, are as follows.")
for key,value in visit_percentages:
    print(f"{key}: {value}%")
