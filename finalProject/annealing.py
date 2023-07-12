#Author: Parker Cuddeback

# solves sudoku with simulated annealing

from math import exp
from random import *
from sudoku import *

# generates a random action
# the random actions are swapping two random non-constant numbers within each block
def random_action(available_index):

    block = random.randint(0, 8)

    usable = len(available_index[block]) - 1

    # grab two tuples from available_index to swap
    swap1 = randint(0, usable)
    swap2 = randint(0, usable)

    # check if they are the same and change if they are
    while swap1 == swap2:
        swap2 = randint(0, usable)

    # unpacking the index of the two values we want to swap
    (row1, col1) = available_index[block][swap1]
    (row2, col2) = available_index[block][swap2]

    return (row1, col1), (row2, col2)


# Each state is represented by an empty board with only constants in it
# Considers a random change at each step.
# Accepts all positive changes and some negative changes.
# Stops after finding a goal state or reaching the minimum temperature.
# Returns the number of steps taken.
def simulated_annealing(state, min_temp, cooling_rate):
    available_index, full, _, _ = board_fill(state)
    current_height = -h(full)
    temperature = 100.0
    steps = 0

    while temperature > min_temp and current_height < 0:
        action = random_action(available_index)
        do(full, action)
        height = -h(full)
        temperature *= cooling_rate
        height_diff = height - current_height

        try:
            probability = exp(height_diff / temperature)
        except:
            print(height)
            print(current_height)
            print(height_diff)
            print(temperature)

        if height > current_height or random.random() < probability:
            current_height = height
            steps += 1
        else:
            undo(full, action)

    return steps, full


