import gym

# With '-v1', the environemnt comes with 500 timesteps.
# In contrast, the environment with '-v2' comes with 200 timesteps.
env = gym.make('CartPole-v1')