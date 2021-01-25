import gym
import numpy as np
from random import random

# With '-v1', the environemnt comes with 500 timesteps.
# In contrast, the environment with '-v2' comes with 200 timesteps.
env = gym.make('CartPole-v1')
print(env._max_episode_steps)

def select_action_random(state):
    if random() < 0.5:
        return 0
    else:
        return 1

def select_action_simple(state):
    if random() < 0.5:
        return 0
    else:
        return 1

def goodness_score(select_action, num_episodes = 100):
    num_steps = 500
    ts = []
    for episode in range(num_episodes):
        state = env.reset()
        for t in range(1, num_steps + 1):
            action = select_action(state)
            state, _, done, _ = env.step(action)
            if done:
                break
        ts.append(t)
    score = sum(ts) / (len(ts) * num_steps)
    return score

print("Score for the RANDOM policy: %f" % goodness_score(select_action_random))
print("Score for the SIMPLE policy: %f" % goodness_score(select_action_simple))

while True:
    action = select_action(state)
    staet, _, done, _ = env.step()
    env.render()
    if done:
        break

