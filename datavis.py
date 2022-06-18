import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

from IOHandler import read_file_to_player_array_array

OFFSET = 0.2

# Make Labels
labels = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
str_label = list(map(str, labels))

X_axis = np.arange(len(str_label))

def overallRawVis():
    # Deck Drawing Technique
    scoreDeckShuffleData = read_file_to_player_array_array("data/deckShuffleData.csv")
    rawDeckShuffleData = reduce(lambda z, y: z + y, scoreDeckShuffleData)
    totals = np.zeros(16, dtype=int)
    for score in rawDeckShuffleData:
        totals[score - 3] = totals[score - 3] + 1
    percent_total = list(map(lambda x: x/len(scoreDeckShuffleData), totals))
    plt.bar(X_axis - 0.2, percent_total, 0.4, label = "Deck Shuffle")

    # 4d6 drop lowest
    scoreDropData = read_file_to_player_array_array("data/dropLow4d6Data.csv")
    rawDropData = reduce(lambda z, y: z + y, scoreDropData)
    totals = np.zeros(16, dtype=int)
    for score in rawDropData:
        totals[score - 3] = totals[score - 3] + 1
    #print(totals)
    percent_total = list(map(lambda x: x/len(scoreDropData), totals))
    plt.bar(X_axis + 0.2, percent_total, 0.4, label = "4d6 drop low")

    # Make Bar Graph

    plt.xticks(X_axis, str_label)
    plt.xlabel("Ability Score")
    plt.ylabel("Odds of getting for a given stat")
    plt.title("Comparing Ability Score Generation Techniques")
    plt.legend()

    plt.show()

#overallRawVis()    