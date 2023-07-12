from _collections import deque
from time import time

# Implements the peg swap puzzle problem with n red pegs
# and n white pegs with one empty spot in the middle.



# Returns the list pf available moves.
def actions_list(state):
    actions = list()
    i = state.index("empty")

    if 0 < i < len(state) - 1:
        if state[i - 1] == "white":
            actions.append((i, i - 1))
        if state[i + 1] == "red":
            actions.append((i, i + 1))

    else:
        if i == 0:
            if state[i + 1] == "red":
                actions.append((i, i + 1))
        if i == len(state) - 1:
            if state[i - 1] == "white":
                actions.append((i, i - 1))

    if 1 < i < len(state) - 2:
        if state[i - 2] == "white" and state[i - 1] == "red":
            actions.append((i, i - 2))
        if state[i + 2] == "red" and state[i + 1] == "white":
            actions.append((i, i + 2))


    else:
        if 0 <= i <= 1:
            if state[i + 1] == "white" and state[i + 2] == "red":
                actions.append((i, i + 2))
        if len(state) - 2 <= i <= len(state) - 1:
            if state[i - 1] == "red" and state[i - 2] == "white":
                actions.append((i, i - 2))

    return actions

# Returns the state reached by an action.
def next_state(state, action):
    i, j = action
    next = list(state)
    next[i], next[j] = next[j], next[i]
    return tuple(next)

# checks for a goal state
def is_goal(state):
    for i in range(0, len(state) - 1):
        if i < (len(state) / 2) - 1:
            if state[i] != "red":
                return False
        elif i == (len(state) / 2):
            if state[i] != 0:
                return False
        elif i > (len(state) / 2):
            if state[i] != "white":
                return False
        else:
            return True

# Heuristic algorithm that counts the number of moves needed in order to move all red/white directly to
# their goal state without regarding any movement restrictions.

def h(state):
    count = 0
    for i in range(0, len(state) - 1):
        if i < (len(state) / 2) - 1:
            if state[i] != "red":
                count += 1
        elif i > (len(state) / 2):
            if state[i] != "white":
                count += 1
        else:
            return count