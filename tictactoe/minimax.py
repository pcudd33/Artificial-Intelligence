# plays tic-tac-toe with minimax.
from problem import *
from math import inf

# Returns the value and the best action for the MAX player
def max_value(state, alpha, beta):
    u = utility(state)
    if u is not None:
        return u, None

    v, move = -inf, None
    for a in actions_list(state):
        # v2 is the utility that we will end up with after this move
        # a2 is the action that our opponent will make
        v2, a2 = min_value(max_next_state(state, a), alpha, beta)
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
            # This is the pruning aspect, this happened when alpha and beta have met
        if v >= beta:
            return v, move
    return v, move


# Returns the value and the best action for the MIN player
# all comments above apply to the code below just for the opposite player
def min_value(state, alpha, beta):
    u = utility(state)
    if u is not None:
        return u, None

    v, move = inf, None
    for a in actions_list(state):
        v2, a2 = max_value(min_next_state(state, a), alpha, beta)
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alpha:
            return v, move
    return v, move

s = (-1, 1, 0,
     1, 1, -1,
     -1, 0, 1)

print(min_value(s, -inf, inf))
