import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

from IOHandler import read_file_to_player_array_array



# Make Chart Labels

## Per score, ie what is the probability of getting a certain score, doesn't make sense in card draw context, but does in 4d6 drop low
per_score_labels = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
per_score_str_label = list(map(str, per_score_labels))
per_score_X_axis = np.arange(len(per_score_str_label))

## Per Build, ie what is the distribution of scores likely to be (sorted) in a given build, makes sense for card draw, but not 4d6 drop low
per_bulid_labels = ["S1", "S2", "S3", "S4", "S5", "S6"]
per_build_X_axis = np.arange(len(per_bulid_labels))

files = ["data/deckShuffleData.csv", "data/dropLow4d6Data.csv"]
filelabels = ["Deck Shuffle", "4d6 Drop Lowest"]
score_data = []
raw_flat_data = []
for dataset in files:
    temp = read_file_to_player_array_array(dataset)
    score_data.append(temp)
    raw_flat_data.append(reduce(lambda z, y: z + y, temp))

TOTAL_BAR_WIDTH = 0.8
num_files = len(files)
bar_width = TOTAL_BAR_WIDTH / num_files
x_offset = bar_width / 2
# creates sequential array of ints, then multiplies each by with of bar, and offsets them because label offset is centered (so we offset by half width of bar)
label_offsets = list(map(lambda x: (x * bar_width) + x_offset - (TOTAL_BAR_WIDTH / 2), np.arange(num_files)))
print(label_offsets)

def sixStackVis():
    num_files = len(files)
    for i in range(0, num_files):
        totals = np.zeros(6, dtype=int)
        dataset = score_data[i]
        for build in dataset:
            build.sort()
            for j in range(0, 6):
                totals[j] = totals[j] + build[j]
        avg_total = list(map(lambda x : x / len(dataset), totals))
        plt.bar(per_build_X_axis + label_offsets[i], avg_total, TOTAL_BAR_WIDTH / num_files, label = filelabels[i])

    plt.xticks(per_build_X_axis, per_bulid_labels)
    plt.xlabel("Build, sorted low to high")
    plt.ylabel("Ability Score Value")
    plt.title("Comparing Ability Score Generation Techniques")
    plt.legend()
    plt.show()

def overallRawVis():
    num_files = len(files)
    for i in range(0, num_files):
        totals = np.zeros(16, dtype=int)
        for score in raw_flat_data[i]:
            totals[score - 3] = totals[score - 3] + 1
        percent_total = list(map(lambda x: x/len(raw_flat_data[i]), totals))
        plt.bar(per_score_X_axis + label_offsets[i], percent_total, TOTAL_BAR_WIDTH / num_files, label = filelabels[i])

    plt.xticks(per_score_X_axis, per_score_str_label)
    plt.xlabel("Ability Score")
    plt.ylabel("Odds of getting a given value for a single stat")
    plt.title("Comparing Ability Score Generation Techniques")
    plt.legend()
    plt.show()

#overallRawVis()
#sixStackVis()