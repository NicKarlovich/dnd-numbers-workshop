import math
import random
from IOHandler import *

def create_player_array():
    i = 0
    j = 0
    player_array = []
    while i < 6:
        # roll 4d6
        score = [random.randint(1,6),  random.randint(1,6), 
                    random.randint(1,6), random.randint(1,6)]
        
        #drop the lowest element
        score.pop(score.index(min(score)))
        
        #append to player array
        player_array.append(sum(score))
        i+= 1
    return player_array

#print(create_player_array())

def create_4d6_stats(num_iter, filename):
    to_write = []
    for i in range(0, num_iter):
        out = create_player_array()
        to_write.append(out)
    write_player_array_array_to_file(filename, to_write)