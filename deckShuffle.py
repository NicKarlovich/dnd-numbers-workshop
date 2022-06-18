import math
import random
from IOHandler import *

card_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 4, '6': 4}

'''
Step 1: To start you take your stack of 18 CARDS, this is called the DECK
Step 2: Shuffle your DECK
Step 3: In any way you want place the cards face-down into 6 piles of 3 cards.
    * Each pile of 3 cards is called a SCORE
    * A set of 6 SCORES makes up a BUILD
    -> This program just splits the DECK based on the order the values appear in the shuffled array
    but if you were doing this with real cards, you could deal them out however you like, 
    as long as each SCORE has exactly 3 cards.
Step 4: Reveal the cards in each SCORE
Step 5: Sum up the value of the cards in each SCORE, this is the SCORE's VALUE, an array of SCORE VALUEs is called a PLAYER ARRAY
Step 6: Find the SCORE(s) with the highest and lowest VALUE(s) and place them in the HIGH TRADE
    and LOW TRADE categories respectively, while keeping each individual SCORE's organization
Step 7: Find the lowest valued CARD in a SCORE in the HIGH TRADE category which we'll call L
Step 8: Find the highest valued CARD in a SCORE in the LOW TRADE category which we'll call H
    * For steps 7 & 8, ties don't matter, so just find the largest CARD, it doesn't matter what score it is in.
Step 9: If L is greater than H, then you may swap the CARDS between the two SCORES, and only those two SCORES
    * Basically this step makes your best score better, and your worst score worse.
DONE!
'''

# Turns dictionary into array, 
def create_deck(card_dict):
    count = 0
    deck = []
    for entry in card_dict:
        #print(str(key) + " " + str(val))
        #print(str(entry) + ": " + str(card_dict[entry]))
        count = count + card_dict[entry]
        for i in range(0, card_dict[entry]):
            deck.append(int(entry))

    if count != 18:
        print("Wrongly sized card_dict, expected size: 18, is " + str(count))
        exit(1)

    return deck

# Splits array of 18 values into 6 SCORES, each representing an ability score of a character
def create_build(deck):
    build = [None, None, None, None, None, None]
    build[0] = deck[:3]
    build[1] = deck[3:6]
    build[2] = deck[6:9]
    build[3] = deck[9:12]
    build[4] = deck[12:15]
    build[5] = deck[15:]
    return build

# isMax == true, finds max scores, isMax == False finds min scores
# returns ALL indices of the SCORES in a build which are either the max or min of the build (depending on param)
def find_boundry_score_idx(build, isMax=True):
    if isMax:
        boundary_val = max(build)
    else:
        boundary_val = min(build)
    output = []
    for i in range(0, len(build)):
        if build[i] == boundary_val:
            output.append(i)
    return output

# Given a set of SCORE's with the same total value, it finds the largest individual CARD and returns it's value and location in the BUILD and SCORE
def find_boundary_idx_card_in_sets(build, boundry_idx_arr, lookingForMax=True):
    
    #Init defautl values
    build_idx = -1
    if lookingForMax:
        boundary_value = -math.inf
    else:
        boundary_value = math.inf

    # looks through all scores, given by their idx in the build
    for i in range(0, len(boundry_idx_arr)):
        score = build[boundry_idx_arr[i]]
        if lookingForMax:
            val = max(score)
            if val > boundary_value:
                build_idx = boundry_idx_arr[i]
                boundary_value = val
                score_idx = score.index(val)
        else:
            val = min(score)
            if val < boundary_value:
                build_idx = boundry_idx_arr[i]
                boundary_value = val
                score_idx = score.index(val)

    return ((build_idx, score_idx), boundary_value)

# Swaps two CARDS in two different scores
def swap_min_max_vars(build, swap1, swap2):
    temp = build[swap1[0]][swap1[1]]
    build[swap1[0]][swap1[1]] = build[swap2[0]][swap2[1]]
    build[swap2[0]][swap2[1]] = temp
    return build

# Does the logic of combining SCORES into PLAYER ARRAYS and the min-max swap if wanted.
def card_swap_logic(build, do_min_max_swap=True):
    player_array = []
    for score in build:
        player_array.append(score[0] + score[1] + score[2])
    if (do_min_max_swap):
        max_score_idx = find_boundry_score_idx(player_array, True)                              # find all sets of cards with max value
        min_score_idx = find_boundry_score_idx(player_array, False)                             # find all sets of cards with min value
        (upperCoords, upperVal) = find_boundary_idx_card_in_sets(build, max_score_idx, False)   # find min value amongst those sets and get ready to swap
        (lowerCoords, lowerVal) = find_boundary_idx_card_in_sets(build, min_score_idx, True)    # find max value amongst min sets and get ready to swap

        #if upper value swapped is less than lower, then doing the swap will maximize one value and min another, vice versa, 
        if upperVal < lowerVal: 
            build = swap_min_max_vars(build, upperCoords, lowerCoords)
            #print("did swap")
#        else:
            #print("didn't swap")

        # recreate player_array with new scores after swap
        player_array = []
        for score in build:
            player_array.append(score[0] + score[1] + score[2])
    return player_array

def create_deck_shuffle_stats(num_iter, filename):
    to_write = []
    for i in range(0, num_iter):
        deck = create_deck(card_dict)
        random.shuffle(deck)
        build = create_build(deck)
        player_array = card_swap_logic(build)
        to_write.append(player_array)
    write_player_array_array_to_file(filename, to_write)

