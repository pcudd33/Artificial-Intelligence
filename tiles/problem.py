# implements nxn tile problem
# Example state: (8, 0, 6, 5, 4, 7, 2, 3, 1)

# Returns a list of actions available
def action_list(state):
    actions = list()

    # index of 0
    i = state.index(0)
    n = int(len(state) ** 0.5)
    row = i // n
    col = i % n

    if row > 0:
        actions.append((i, i - n))
    if row < n - 1:
        actions.append((i, i + n))
    if col > 0:
        actions.append((i, i - 1))
    if col < n - 1:
        actions.append((i, i + 1))

    return actions


# Returns the state reached by an actions.
def next_state(state, action):
    i, j = action
    next = list(state)
    next[i], next[j] = next[j], next[i]
    return tuple(next)


# Checks for a goal state.
def is_goal(state):
    for i in range(len(state)):
        if state[i] != i:
            return False
    return True

# Return the manhattan distance heuristic
def h(state):
    n = int(len(state) ** 0.5)
    total = 0

    for i in range(len(state)):
        if state[i] > 0:
            row = i // n
            goal_row = state[i] // n
            total += abs(row - goal_row)

            col = i % n
            goal_col = state[i] % n
            total +=  abs(col - goal_col)

    return total

print(h(()))