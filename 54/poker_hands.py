from math import factorial
from math import comb as binom
import numpy as np

card_ranks = {
    "High Card" : 0,
    "One Pair" : 1,
    "Two Pairs" : 2,
    "Three of a Kind" : 3,
    "Straight" : 4,
    "Flush" : 5,
    "Full House" : 6,
    "Four of a Kind" : 7,
    "Straight Flush" : 8,
    "Royal Flush" : 9
}

card_values = dict(
        [(str(i), i) for i in range(2,10)] +
        [("T", 10), ("J", 11), ("Q", 12), ("K", 13), ("A", 14)]
)

def test_consecutive_values(card_names : list[str]) -> bool:
    if(len(set(card_names)) != 5):
        return False
    values = [card_values[card_name] for card_name in card_names]
    return (min(values) == max(values) - 4)

def rank_hand(cards : list[str]) -> tuple[int, int, int]:
    """
    Returns the rank of the hand, the value of the highest card contributing to the rank,
    and the value of the highest card from the rest of the cards.
    """
    card_names = [card[0] for card in cards]
    card_suits = [card[1] for card in cards]
    highest_card = max(card_names, key=lambda name: card_values[name])
    highest_value = card_values[highest_card]
    same_suit = (len(set(card_suits)) == 1)
    cards_are_consecutive = test_consecutive_values(card_names)
    highest_count = max([card_names.count(name) for name in set(card_names)])

    if(same_suit and cards_are_consecutive):
        if("A" in card_names):
            return (card_ranks["Royal Flush"], card_values("A"), card_values("A"))
        else:
            return (card_ranks["Straight Flush"], highest_value, highest_value) 
    if(len(set(card_names)) == 2):
        if(card_names.count(card_names[0]) == 4):
            return (card_ranks["Four of a Kind"],
                    card_values[card_names[0]],
                    card_values[card_names[1]]
            )
        if(card_names.count(card_names[1]) == 4):
            return (card_ranks["Four of a Kind"],
                    card_values[card_names[1]],
                    card_values[card_names[0]]
            )
        triple_card = [name for name in card_names if card_names.count(name) == 3][0]
        double_card = [name for name in card_names if card_names.count(name) == 2][0]
        return (card_ranks["Full House"],
                card_values[triple_card],
                card_values[double_card]
        )
    if(same_suit):
        return (card_ranks["Flush"], highest_value, highest_value)
    if(cards_are_consecutive):
        return (card_ranks["Straight"], highest_value, highest_value)
    if(len(set(card_names)) == 3):
        if(highest_count == 3):
            triple_card = max(card_names, key = card_names.count)
            other_highest_value = max(
                    [card_values[name] for name in card_names if name != triple_card]
            )
            return (card_ranks["Three of a Kind"],
                    card_values[triple_card],
                    other_highest_value
            )
        double_cards = [name for name in set(card_names) if card_names.count(name) == 2]
        single_card = [name for name in set(card_names) if card_names.count(name) == 1][0]
        return (
                card_ranks["Two Pairs"],
                max(card_values[double_cards[0]], card_values[double_cards[1]]),
                card_values[single_card]
        )
    if(highest_count == 2):
        double_card = max(card_names, key = card_names.count)
        other_cards = [name for name in card_names if card_names.count(name) == 1]
        highest_other_value = max([card_values[name] for name in other_cards])
        return (card_ranks["One Pair"], card_values[double_card], highest_other_value)
    return (card_ranks["High Card"], highest_value, highest_value)

def compare_ranks(rank_1 : tuple[int,int,int], rank_2 : tuple[int,int,int]) -> int:
    for i in range(3):
        if(rank_1[i] > rank_2[i]):
            return 1
        if(rank_2[i] > rank_1[i]):
            return 2
    return 0

if __name__ == "__main__":
    '''
    examples = [
        [["5H", "5C", "6S", "7S", "KD"], ["2C", "3S", "8S", "8D", "TD"]],
        [["5D", "8C", "9S", "JS", "AC"], ["2C", "5C", "7D", "8S", "QH"]],
        [["2D", "9C", "AS", "AH", "AC"], ["3D", "6D", "7D", "TD", "QD"]],
        [["4D", "6S", "9H", "QH", "QC"], ["3D", "6D", "7H", "QD", "QS"]],
        [["2H", "2D", "4C", "4D", "4S"], ["3C", "3D", "3S", "9D", "9S"]]
    ]
    for game in examples:
        print(game)
        ranks = rank_hand(game[0]), rank_hand(game[1])
        print(ranks)
        comp = compare_ranks(ranks[0], ranks[1])
        print(comp)
    '''  

    with open("poker.txt", "r") as file:
        games = file.readlines()
    count = 0
    for line in games:
        cards = line[:-1].split(" ")
        hands = cards[:5], cards[5:]
        ranks = [rank_hand(hand) for hand in hands]
        count += (compare_ranks(ranks[0], ranks[1]) == 1)
    print(count)
         
