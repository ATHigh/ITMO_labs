import ray
from ray import tune
from ray.rllib.algorithms.ppo import PPOConfig
import gymnasium as gym
from cartpole_env import CartPoleLeftRight

local_mode = False
num_workers = 4

ray.init(local_mode=local_mode)


def create_env(env_config):
    env = CartPoleLeftRight(render_mode="human")
    return env

tune.register_env(
    "my_env",
    create_env,
)

config = (
    PPOConfig()
    .environment(
        env="my_env",
    )
    .framework("torch")
    .rollouts(
        num_env_runners=num_workers if not local_mode else 0,
        batch_mode="complete_episodes"
    )
    .training(
        lr=0.0003,
        lambda_=0.95,
        gamma=0.99,
        sgd_minibatch_size=512,
        train_batch_size=2000*4,
        num_sgd_iter=8,
        vf_loss_coeff=1.0,
        kl_coeff=0.01,
        clip_param=0.2,
        entropy_coeff=0.001,
        grad_clip=10,
        model={
            "fcnet_hiddens": [256, 128],
            "vf_share_layers": True,
        },
    )
    .resources(num_gpus=1)
    .debugging(log_level="INFO")
)
stop = {
    "training_iteration": 9999999999,
    "timesteps_total": 1000000,
    "episode_reward_mean": 999999999,
}

tune.run(
    "PPO",
    config=config.to_dict(),
    stop=stop,
    verbose=3,
    checkpoint_freq=10,
    checkpoint_at_end=True,
)

ray.shutdown()