# solves tile puzzles with breadth-first search.
from problem import *
from _collections import deque
from time import time

# Gets a pth out of a search tree.
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

        for action in action_list(state):
            next = next_state(state, action)

            if next not in parent:
                parent[next] = state

                if is_goal(next):
                    # return the path from start to next
                    return extract_path(next, parent)
                else:
                    frontier.append(next)

# Hardest 3x3 puzzle (d=31)
before = time()
start_state = (8, 0, 6, 5, 4, 7, 2, 3, 1)
path_to_goal = breadth_first_search(start_state)
print("found a solution at depth", len(path_to_goal) - 1, "in", time() - before, "seconds.")

# Easy 4x4 puzzle (d=80)
# this one will take up to much memory DON'T DO IT!!
before = time()
start_state = (15, 14, 8, 12, 10, 11, 9, 13, 2, 6, 5, 1, 3, 7, 4, 0)
path_to_goal = breadth_first_search(start_state)
print("found a solution at depth", len(path_to_goal) - 1, "in", time() - before, "seconds.")