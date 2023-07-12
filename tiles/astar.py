# solves tile puzzles with greedy heuristic search.
from problem import *
from heapdict import heapdict
# Heapdict is a priority queue
from time import time

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
def astar_search(start, w=1):
    frontier = heapdict({start: w * h(start)})
    parent = {start: None}
    g = {start: 0}

    while len(frontier) > 0:
        state, priority = frontier.popitem()

        if is_goal(state):
            return extract_path(state, parent)

        for action in action_list(state):
            next = next_state(state, action)

            if next not in g or g[state] + 1 < g[next]:
                parent[next] = state
                g[next] = g[state] + 1
                frontier[next] = g[next] + w * h(next)



# Hardest 3x3 puzzle (d=31)
before = time()
start_state = (8, 0, 6, 5, 4, 7, 2, 3, 1)
path_to_goal = astar_search(start_state)
print("found a solution at depth", len(path_to_goal) - 1, "in", time() - before, "seconds.")

# Easy 4x4 puzzle (d=80)
before = time()
start_state = (15, 14, 8, 12, 10, 11, 9, 13, 2, 6, 5, 1, 3, 7, 4, 0)
path_to_goal = astar_search(start_state, w=2)
print("found a solution at depth", len(path_to_goal) - 1, "in", time() - before, "seconds.")