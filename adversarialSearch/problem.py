# Implements the game of tic-tac-toe

# Returns an empty board.
def start_state():
    return (0,) * 9 #this creates a tuple of 9 zeros you can also do this with lists [0] * 9 we need a , after to designate it as a tuple.


# Returns a list of actions available.
def actions_list(state):
    #actions = []
    #for i in range(9):
    #   if state[i] == 0:
    #        actions.append(i)
    #return actions
    return [i for i in range(9) if state[i] == 0] # This line does the same thing as the loops above

# Returns the state reached by placing an X.
def max_next_state(state, action):
    return state[:action] + (1,) + state[action + 1:]

# Returns the state reached by placing an O.
def min_next_state(state, action):
    return state[:action] + (-1,) + state[action + 1:]


# Returns +1 for an X win, -1 for an O win, 0 for a tie, None for a non-terminal state
# when slicing the last index of the tuple does not get included
# when there are three numbers within the slice the third iterates
def utility(state):
   lines = [state[0:3], state[3:6], state[6:9],         # rows
            state[0:7:3], state[1:8:3], state[2:9:3],   # columns
            state[0:9:4], state[2:7:2]]                 # diagonals

   if (1, 1, 1) in lines:
       return 1
   elif (-1, -1, -1) in lines:
       return -1
   elif 0 not in state:
       return 0




s = (0,0,0,
     0,0,0,
     1,1,1)

