# Solves queens puzzles with simulated annealing.
from problem import *
from math import exp
from random import randint, random


# Generates a random action.
def random_action(state):
    n = len(state)
    i = randint(0, n - 2)
    j = randint(i + 1, n - 1)
    return i, j


# Considers a random change at each step.
# Accepts all positive changes and some negative changes.
# Stops after finding a goal state or reaching the minimum temperature.
# Returns the number of steps taken.
def simulated_annealing(state, min_temp, cooling_rate):
    current_height = -h(state)
    temperature = 100.0
    steps = 0

    while temperature > min_temp and current_height < 0:
        action = random_action(state)
        do(state, action)
        height = -h(state)

        temperature *= cooling_rate
        height_diff = height - current_height
        probability = exp(height_diff / temperature)

        if height > current_height or random() < probability:
            current_height = height
            steps += 1
        else:
            undo(state, action)

    return steps


# A few attempts
for test in range(10):
    s = random_state(16)
    steps_taken = simulated_annealing(s, 0.1, 0.999)
    print("Stopped at", h(s), "attacking pairs after", steps_taken, "steps.")


