# plays tic-tac-toe with minimax.
from problem import *
from math import inf


# Returns the value and the best action for the MAX player
def max_value(state, alpha, beta, depth):

    u = utility(state)
    if u is not None:
        return u, None
    v, move = -inf, None
    if depth == 0:
        return evaluation_function(state), None
    depth -= 1
    for a in actions_list(state):
        # v2 is the utility that we will end up with after this move
        # a2 is the action that our opponent will make
        v2, a2 = min_value(max_next_state(state, a), alpha, beta, depth)
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
            # This is the pruning aspect, this happened when alpha and beta have met
        if v >= beta:
            return v, move

    return v, move


# Returns the value and the best action for the MIN player
# all comments above apply to the code below just for the opposite player
def min_value(state, alpha, beta, depth):
    u = utility(state)
    if u is not None:
        return u, None
    v, move = inf, None
    if depth == 0:
        return evaluation_function(state), None
    depth -= 1
    for a in actions_list(state):
        v2, a2 = max_value(min_next_state(state, a), alpha, beta, depth)
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alpha:
            return v, move

    return v, move


def evaluation_function(state):
    lines = [state[0:3], state[3:6], state[6:9],  # rows
             state[0:7:3], state[1:8:3], state[2:9:3],  # columns
             state[0:9:4], state[2:7:2]]  # diagonals

    # Two 1 and one 0 = .5 Two -1 and one 0 = .5
    # one 1 and two 0 = .25 one -1 and one 0 = .25
    numerator = 0
    denominator = 0

    for line in lines:
        if line == (1, 1, 0) or line == (1, 0, 1) or line == (0, 1, 1):
            numerator += 2 * .5
            denominator += .5
        elif line == (-1, -1, 0) or line == (-1, 0, -1) or line == (0, -1, -1):
            numerator += 2 * -.5
            denominator += .5
        elif line == (1, 0, 0) or line == (0, 1, 0) or line == (0, 0, 1):
            numerator += 1 * .25
            denominator += .25
        elif line == (-1, 0, 0) or line == (0, -1, 0) or line == (0, 0, -1):
            numerator += 1 * -.25
            denominator += .25

    if numerator == 0 or denominator == 0:
        return 0

    return numerator / (denominator + 1)


