# Q-learning in the non-slippery version of Frozen lake
import gym
import matplotlib.pyplot as plt
from random import random, choice

# Environment
env = gym.make("FrozenLake-v1", is_slippery=False)
states = list(range(env.observation_space.n))
actions = list(range(env.action_space.n))

# Settings
epsilon = 0.1  # at the beginning we will be intentionally exploring 10% of the time
alpha = 0.3
gamma = 0.9    # we care about future rewards a little bit so eventually we will find the terminal state

# Q-values
Q = {(s, a): 0.0 for s in states for a in actions}

# Schedule
batches = list(range(20))    # outer iterations
episodes = list(range(10))   # inner iterations
successes = [0 for batch in batches]    # this array keeps track of the successes in each batch

# Training
for batch in batches:
    for episode in episodes:
        s, info = env.reset()
        while True:

            # Choose an action
            if random() <= epsilon:
                a = choice(actions)
            else:
                best_Q = max(Q[s, a] for a in actions)
                # give me all the actions where the q_value = best_q
                best_actions = [a for a in actions if Q[s, a] == best_Q]
                # randomly choose from all the best_qs
                a = choice(best_actions)

            # Take the action
            # sp = next state
            # r = reward
            # if either below are true the game is over
            # terminated = did the game end
            # truncated = the maximum number fo steps reached
            sp, r, terminated, truncated, info = env.step(a)

            # Updates after each step
            # This is the formula without the future reward because the game has ended
            if terminated or truncated:
                Q[s, a] = alpha * r + (1 - alpha) * Q[s, a]
                break
            else:
                Q[s, a] = alpha * (r + gamma * max(Q[sp, ap] for ap in actions)) + (1 - alpha) * Q[s, a]
                # update the state
                s = sp

        # Updates after each episode
        successes[batch] += r
        # these are the decay rates for epsilon and alpha
        epsilon *= 0.9
        alpha *= 0.9

# Results
plt.plot(batches, successes)
plt.ylabel("Successes per batch")
plt.xlabel("Batch number")
plt.show()
