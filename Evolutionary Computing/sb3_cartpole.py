import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

from cartpole_env import CartPoleLeftRight, CartPoleEnv
from stable_baselines3.common.callbacks import CheckpointCallback

# Save a checkpoint every 1000 steps
checkpoint_callback = CheckpointCallback(
  save_freq=20000,
  save_path="./logs/",
  name_prefix="rl_model",
  save_replay_buffer=True,
  save_vecnormalize=True,
)

def setup_env():
    return CartPoleLeftRight()
    # return CartPoleEnv()

# Parallel environments
vec_env = make_vec_env(setup_env, n_envs=4)

model = PPO("MlpPolicy", vec_env, verbose=1, tensorboard_log="./ppo_cartpole_tensorboard/")
model.learn(total_timesteps=1000000, callback=checkpoint_callback)
model.save("ppo_cartpole")

obs = vec_env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")