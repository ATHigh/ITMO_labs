import os
import pickle
import ray
from ray import tune
from ray.rllib.algorithms.ppo import PPO
import gymnasium as gym
from cartpole_env import CartPoleLeftRight

def create_env(env_config):
    env = CartPoleLeftRight(render_mode='human')
    return env

def read_config(checkpoint_path) -> dict:
    with open(os.path.join(checkpoint_path, "algorithm_state.pkl"), 'rb') as file:
        config = pickle.load(file)
    return config

checkpoint_path = "/Users/roman14/Desktop/Pycharm/ITMO_labs/Evolutionary Computing/Task2/results/PPO_2024-10-29_18-16-12/PPO_my_env_59a92_00000_0_2024-10-29_18-16-12/checkpoint_000042"

ray.init(local_mode=True)

exp_config = read_config(checkpoint_path)['config']
exp_config['num_workers'] = 0

tune.register_env(
    "my_env",
    create_env,
)

agent = PPO(exp_config)
agent.load_checkpoint(checkpoint_path)
policy = agent.get_policy()

env = create_env({})

for _ in range(1000):
    state = env.reset()[0]
    for _ in range(300):
        act = agent.compute_single_action(state)
        state, r, d, tr, i = env.step(act)
        if d:
            break

ray.shutdown()
