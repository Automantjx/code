import gym
import numpy as np
from random import random
import torch
from torch.nn import functional
from dqn_agent import DQNAgent

env = gym.make('CartPole-v1')
s, _ = env.reset()
n_state = len(s)
n_action = env.action_space.n
agent = DQNAgent(n_input=n_state, n_output=n_action)

n_episode = 5000
n_step = 1000
TARGET_UPDATE_FREQUENCY = 100
EPSILON_DECAY = 10000
EPSILON_START = 1.0
EPSILON_END = 0.02
REWARD_BUFFER = np.empty(shape=n_episode)


for episode_i in range(n_episode):
    episode_reward = 0
    
    for step_i in range(n_step):
        epsilon = np.interp(episode_i * n_step + step_i, [0, EPSILON_DECAY], [EPSILON_START, EPSILON_END])
        random_sample = random()
        
        if random_sample <= epsilon:
            a = env.action_space.sample()
        else:
            a = agent.online_net.act(s)
            
        s_, r, done, truncated, info = env.step(a)
        agent.memo.add_memo(s, a, r, done, s_)
        s = s_
        episode_reward += r
        
        if done:
            s,_ = env.reset()
            REWARD_BUFFER[episode_i] = episode_reward
            break
        
        batch_s, batch_a, batch_r, batch_done, batch_s_ = agent.memo.sample()
        
        # compute targets
        target_q_values = agent.target_net(batch_s_)
        max_target_q_values = target_q_values.max(dim=1)[0]
        targets = batch_r + agent.GAMMA * (1-batch_done) * max_target_q_values
        
        # compute q_values
        q_values = agent.online_net(batch_s)
        a_q_values = torch.gather(input=q_values, dim=1, index=batch_a)
        
        # compute loss
        loss = functional.smooth_l1_loss(targets, a_q_values)
        
        # gradient descent
        agent.optimizer.zero_grad()
        loss.backward()
        agent.optimizer.step()
        
    if episode_i % TARGET_UPDATE_FREQUENCY == 0:
        agent.target_net.load_state_dict(agent.online_net.state_dict())
        
        print(f"Episode:{episode_i}.")
        print(f"The avg of reward is {np.mean(REWARD_BUFFER[:episode_i])}")
        