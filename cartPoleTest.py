import gym

# With '-v1', the environemnt comes with 500 timesteps.
# In contrast, the environment with '-v2' comes with 200 timesteps.
env = gym.make('CartPole-v1')

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
    for episode in range(num_episode):
        for t in range(1, num_step + 1):
            action = select_action(state)
            state, _, done, _ = env.step(action)
            if done:
                break
        ts.append(t)
    score = sum(ts) / len(ts) * num_steps)
    return score

while True:
    action = select_action(state)
    staet, _, done, _ = env.step()
    env.render()
    if done:
        break

