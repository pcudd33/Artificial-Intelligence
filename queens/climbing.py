# Solves queens puzzles with hill-climbing
from problem import *

# Makes the biggest improvement possible at each step.
# Stops when no further improvements are possible.
# Returns the number of steps taken.
def hill_climbing(state):
    steps = 0

    while True:
        best_height = -h(state)         # -h(state) is our starting state
        best_action = None              # there could be a state where every action makes it worse

        for action in action_generator(state):
            do(state, action)
            height = -h(state)          # this is negative because the resolved problem is h(0)

            if height > best_height:    # this is greater than bc height is negative
                best_height = height
                best_action = action

            undo(state, action)

        if best_action is not None:
            do(state, best_action)
            steps += 1
        else:
            return steps


for test in range(10):
    s = random_state(16)
    steps_taken = hill_climbing(s)
    print("Stopped at", h(s), "attacking pairs after", steps_taken, "steps.")