from deckShuffle import *
from dropLow4d6 import *
from IOHandler import *

def get_total_points(card_dict):
    tot = 0
    for card in card_dict:
        tot = tot + int(card) * card_dict[card]
    return tot

card_dictA = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 4, '6': 4}     # id: A     original idea, 74 points total 
card_dictB = {'1': 0, '2': 3, '3': 4, '4': 4, '5': 4, '6': 3}     # id: B     original design
card_dictC = {'1': 1, '2': 2, '3': 4, '4': 4, '5': 3, '6': 4}     # id: C     
card_dictD = {'1': 1, '2': 1, '3': 4, '4': 3, '5': 4, '6': 4}     # id: D     

print(get_total_points(card_dictA))
print(get_total_points(card_dictB))
print(get_total_points(card_dictC))
print(get_total_points(card_dictD))

x = 1
if x == 1:
    #NUM_ITER = 1000000 #1mil
    NUM_ITER = 10000
    create_deck_shuffle_stats(NUM_ITER, "data/deckShuffleDataA.csv", card_dictA)
    create_deck_shuffle_stats(NUM_ITER, "data/deckShuffleDataB.csv", card_dictA)
    create_deck_shuffle_stats(NUM_ITER, "data/deckShuffleDataC.csv", card_dictA)
    create_deck_shuffle_stats(NUM_ITER, "data/deckShuffleDataD.csv", card_dictA)
    create_4d6_stats(NUM_ITER, "data/dropLow4d6Data.csv")