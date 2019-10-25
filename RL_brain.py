# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:00:33 2019

@author: yukic
"""

import numpy as np
import pandas as pd

class QLearningTable:
    # initialization
    # actions are provided by list of index
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions # a list
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions)
        
    # i guess observation is our current state
    # algorithm to assign action in each state
    def choose_action(self, observation):
        self.check_state_exist(observation)
        
        # exploitation, choosing actions based on already learned Q-values
        # action selection
        if np.random.uniform() < self.epsilon:
            # choose best action
            state_action = self.q_table.ix[observation, :]
            # minor adjustment
            state_action = state_action.reindex(np.random.permutation(state_action.index)) # some actions have same value
            # action = state_action.argmax()
            # actually assigning what the best action is
            action = state_action.astype(float).idxmax()
            
        # exploration, choosing a random action
        else:
            # choose random action
            action = np.random.choice(self.actions)
        return action
            
    # updating q value algorithm
    def learn(self, s, a, r, s_):
        self.check_state_exist(s_)
        q_predict = self.q_table.ix[s, a]
        if s_ != 'terminal':
            # need this for updating q values. What we can get from the next
            q_target = r + self.gamma * self.q_table.ix[s_, :].max() # next state is not terminal
        else:
            q_target = r # next state is terminal
        # this is the actualy update of q values
        self.q_table.ix[s, a] += self.lr * (q_target - q_predict) # update
            
    # by exploring states, we are expanding our q-table. Initially we only have columns and no rows
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                    pd.Series(
                            [0]*len(self.actions),
                            index=self.q_table.columns,
                            name=state,
                    )
            )
            
            
    
    
    
    
    
    
    
            
            