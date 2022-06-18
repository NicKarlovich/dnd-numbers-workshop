from deckShuffle import *
from dropLow4d6 import *
from IOHandler import *

x = 1
if x == 1:
    #NUM_ITER = 1000000 #1mil
    NUM_ITER = 1000 #1mil
    create_deck_shuffle_stats(NUM_ITER, "data/deckShuffleData.csv")
    create_4d6_stats(NUM_ITER, "data/dropLow4d6Data.csv")