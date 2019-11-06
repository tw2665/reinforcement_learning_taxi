import sys
from contextlib import closing
from six import StringIO
from gym import utils
from gym.envs.toy_text import discrete
from gym import Env, spaces
from gym.utils import seeding
import numpy as np


class NewTaxi(Env):
    
    def __init__(self, n, m, locs):
        self.env = np.zeros((n, m))
        self.n = n
        self.m = m
        # locs is a tuple ([get on], [get off])
        self.locs = locs
        self.state = [np.random.choice(n), np.random.choice(m)]
        self.action_space = {'U': -1, 'D': 1, 'L': -1, 'R': 1}
        self.reward = 0
        self.loaded = None
        
    def reset(self):
        n, m = self.n, self.m
        self.env = np.zeros((n, m))
        self.state = [np.random.choice(n), np.random.choice(m)]
        self.reward = 0
        self.loaded = None
        return self.state
    
    def step(self, action):
        n, m = self.n, self.m
        acts = self.action_space
        load = self.loaded
        reward = self.reward
        old_state = self.state
        # update new state
        if action == 'U' or action == 'D':             
            state = [old_state[0] + acts[action], old_state[1]]
        elif action == 'L' or action == 'R':
            state = [old_state[0], old_state[1] + acts[action]]
        
        # check if hit the wall 
        if state[0] < 0 or state[0] >= n or state[1] < 0 or state[1] >= m:
            reward -= 4 # total lost of reward should be this + 1 
            state = old_state 
        
        done = False
        if load:
            if state == self.locs[1]:
                reward += 5
                done = True
            else: 
                reward -= 1
        elif load is None:
            if state == self.locs[0]:
                reward += 5
            else: 
                reward -= 1
        
        self.state = state
        self.reward = reward
        return state, reward, done # no info return here


    def render(self, mode='human'):
        locs = self.locs
        state = self.state
        env = self.env.copy()
        env[state[0], state[1]] = 1 # taxi pos
        env[locs[0][0], locs[0][1]] = 2 # get on point
        env[locs[1][0], locs[1][1]] = 3 # get off point
        n, m = self.n, self.m
        out = ''

        for i in range(n):
            for j in range(m):
                if env[i, j] == 0:
                    out += '*'
                elif env[i, j] == 1:
                    out += 'X'
                elif env[i, j] == 2:
                    out += 'I'
                elif env[i, j] == 3:
                    out += 'O'
                out += '  '
            out += '\n'

        print(out)
        

