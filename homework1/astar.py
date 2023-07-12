# solves tile puzzles with greedy heuristic search.
from heapdict import heapdict
# Heapdict is a priority queue

from time import time
from _collections import deque

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
        if state[i + 2] == "red" and state[i + 1] == "white":
            actions.append((i, i + 2))
        if state[i - 2] == "white" and state[i - 1] == "red":
            actions.append((i, i - 2))



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


# Gets a path out of a search tree.
def extract_path(state, parent):
    path = [state]
    while parent[state] is not None:
        state = parent[state]
        path.append(state)
    path.reverse()
    return path

# With w=1, returns a shortest path, unless it runs out of memory first.
# With w>1 the path may be longer, but you're also more likely to get one.
def astar_search(start, w= 1):
    frontier = heapdict({start: w * h(start)})
    parent = {start: None}
    g = {start: 0}

    while len(frontier) > 0:
        state, priority = frontier.popitem()

        if is_goal(state):
            return extract_path(state, parent)

        for action in actions_list(state):
            next = next_state(state, action)

            if next not in g or g[state] + 1 < g[next]:
                parent[next] = state
                g[next] = g[state] + 1
                frontier[next] = g[next] + w * h(next)


# designation of pegs and empty space
w = "white"
e = "empty"
r = "red"

# Creating the tuples that contain all pegs and empty spaces
before = time()
start_state = (w, w, e, r, r)
path_to_goal_2 = astar_search(start_state)
print("found a solution at n = 2 and depth is", len(path_to_goal_2), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, e, r, r, r, r)
path_to_goal_4 = astar_search(start_state)
print("found a solution at n = 4 and depth is", len(path_to_goal_4), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, e, r, r, r, r, r, r)
path_to_goal_6 = astar_search(start_state)
print("found a solution at n = 6 and depth is", len(path_to_goal_6), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, w, w, e, r, r, r, r, r, r, r, r)
path_to_goal_8 = astar_search(start_state)
print("found a solution at n = 8 and depth is", len(path_to_goal_8), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, w, w, w, w, e, r, r, r, r, r, r, r, r, r, r)
path_to_goal_10 = astar_search(start_state)
print("found a solution at n = 10 and depth is", len(path_to_goal_10), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, w, w, w, w, w, w, e, r, r, r, r, r, r, r, r, r, r, r, r)
path_to_goal_12 = astar_search(start_state)
print("found a solution at n = 12 and depth is", len(path_to_goal_12), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, w, w, w, w, w, w, w, w, e, r, r, r, r, r, r, r, r, r, r, r, r, r, r)
path_to_goal_14 = astar_search(start_state)
print("found a solution at n = 14 and depth is", len(path_to_goal_14), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, e, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r)
path_to_goal_16 = astar_search(start_state)
print("found a solution at n = 16 and depth is", len(path_to_goal_16), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, e, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r)
path_to_goal_18 = astar_search(start_state)
print("found a solution at n = 18 and depth is", len(path_to_goal_18), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, e, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r)
path_to_goal_20 = astar_search(start_state)
print("found a solution at n = 20 and depth is", len(path_to_goal_20), "in", time() - before, "seconds.")