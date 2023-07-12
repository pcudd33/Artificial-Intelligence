# solves tile puzzles with breadth-first search.
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

def extract_path(state, parent):
    path = [state]
    while parent[state] is not None:
        state = parent[state]
        path.append(state)
    path.reverse()
    return path

# Returns a shortest path to a goal state.
# Unless it runs out of memory first.
def breadth_first_search(start):
    if is_goal(start):
        return [start]

    frontier = deque([start])
    parent = {start: None}

    while len(frontier) > 0:
        state = frontier.popleft()

        for action in actions_list(state):
            next = next_state(state, action)

            if next not in parent:
                parent[next] = state

                if is_goal(next):
                    # return the path from start to next
                    return extract_path(next, parent)
                else:
                    frontier.append(next)


w = "white"
e = "empty"
r = "red"
before = time()
start_state = (w, w, e, r, r)
path_to_goal_2 = breadth_first_search(start_state)
print("found a solution at n = 2 and depth is", len(path_to_goal_2), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, e, r, r, r, r)
path_to_goal_4 = breadth_first_search(start_state)
print("found a solution at n = 4 and depth is", len(path_to_goal_4), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, e, r, r, r, r, r, r)
path_to_goal_6 = breadth_first_search(start_state)
print("found a solution at n = 6 and depth is", len(path_to_goal_6), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, w, w, e, r, r, r, r, r, r, r, r)
path_to_goal_8 = breadth_first_search(start_state)
print("found a solution at n = 8 and depth is", len(path_to_goal_8), "in", time() - before, "seconds.")

before = time()
start_state = (w, w, w, w, w, w, w, w, w, w, e, r, r, r, r, r, r, r, r, r, r)
path_to_goal_10 = breadth_first_search(start_state)
print("found a solution at n = 10 and depth is", len(path_to_goal_10), "in", time() - before, "seconds.")
