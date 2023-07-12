# Implements n-queens puzzles.
from random import shuffle


# Returns a random state.
# n is the number of integers put into the list
def random_state(n):
    # putting the list in front of range creates a list instead of range which is
    # a generator and returns one value at a time
    state = list(range(n))
    shuffle(state)
    return state


# yields a sequence of possible actions.
def action_generator(state):
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            yield i, j      # doesn't stop the functions and allows for it to be used again later


# Changes a state with an action.
def do(state, action):
    i, j = action
    state[i], state[j] = state[j], state[i]


# Restores a state that was changed
def undo(state, action):
    i, j = action
    state[i], state[j] = state[j], state[i]


# Returns the number of attaching pairs.
# The indices within the state array are the rows and the values represent the columns
def h(state):
    n = len(state)
    pairs = 0

    for r1 in range(n):
        c1 = state[r1]
        for r2 in range(r1 + 1, n):
            c2 = state[r2]
            if c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                pairs += 1

    return pairs

#print(h([2, 0, 3, 1]))
#print(h([0, 1, 2, 3]))
