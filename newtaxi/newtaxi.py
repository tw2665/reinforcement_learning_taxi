import sys
from contextlib import closing
from six import StringIO
from gym import utils
from gym.envs.toy_text import discrete
from gym import Env, spaces
from gym.utils import seeding
import numpy as np
from termcolor import colored, cprint


class NewTaxi(Env):
    
    def __init__(self, n, m, locs):
        self.env = np.zeros((n, m))
        self.n = n
        self.m = m
        # locs is a tuple ([get on], [get off])
        self.locs = locs
        # the first is location parameter, the second is loaded with passenger 
        self.state = {'loc':[np.random.choice(n), np.random.choice(m)], 'load':0}
        self.action_space = {'U': -1, 'D': 1, 'L': -1, 'R': 1}
        # set up obs and act space size for q-table
        self.action_space_n = len(self.action_space)
        self.observation_space_n = n*m*len(locs)
        self.reward = 0
        self.loaded = 0
    
    def state2state_id(self, state):
        return (state['loc'][0]*self.n + state['loc'][1]) + (state['load'] * self.n * self.m)
        
    def reset(self):
        n, m = self.n, self.m
        self.env = np.zeros((n, m))
        self.state = {'loc':[np.random.choice(n), np.random.choice(m)], 'load':0}
        self.reward = 0
        self.loaded = False
        return self.state
    
    def step(self, action):
        n, m = self.n, self.m
        acts = self.action_space
        load = self.loaded
        reward = self.reward
        old_state = self.state
        state = {}
        # update new state
        if action == 'U' or action == 'D':             
            state['loc'] = [old_state['loc'][0] + acts[action], old_state['loc'][1]]
        elif action == 'L' or action == 'R':
            state['loc'] = [old_state['loc'][0], old_state['loc'][1] + acts[action]]
        
        # check if hit the wall 
        if state['loc'][0] < 0 or state['loc'][0] >= n or \
                state['loc'][1] < 0 or state['loc'][1] >= m:
            reward -= 4 # total lost of reward should be this + 1 
            state = old_state 
        
        done = False
        if load:
            state['load'] = 1
            if state['loc'] == self.locs[1]:
                reward += 5
                done = True
            else: 
                reward -= 1
        else:
            # check if pick up the passenger
            if state['loc'] == self.locs[0]:
                reward += 5
                load = 1
                state['load'] = 1
            else: 
                reward -= 1
                state['load'] = 0
        
        self.state = state
        self.reward = reward
        self.loaded = load
        return state, reward, done # no info return here


    def render(self, mode='human'):
        locs = self.locs
        state = self.state
        env = self.env.copy()
        load = state['load'] 
        env[state['loc'][0], state['loc'][1]] = 1 # taxi pos
        env[locs[0][0], locs[0][1]] = 2 # get on point
        env[locs[1][0], locs[1][1]] = 3 # get off point
        n, m = self.n, self.m
        out = ''

        for i in range(n):
            for j in range(m):
                if env[i, j] == 0:
                    out += '*'
                elif env[i, j] == 1:
                    if load == 1:
                        out += colored('X', 'red')
                    else:
                        out += colored('X', 'yellow')
                elif env[i, j] == 2:
                    if load == 1:
                        out += colored('I', 'red')
                    else:
                        out += colored('I', 'green')
                elif env[i, j] == 3:
                    out += 'O'
                out += '  '
            out += '\n'

        print(out)
        

