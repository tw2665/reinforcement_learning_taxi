# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:11:36 2019

@author: yukic
"""

### directory setting
import os
my_path = "/Users/liweizhang/Columbia University/cu_semester2/GitHub/AML-Project-"
os.chdir(my_path)
###

from maze_env import Maze
from RL_brain import QLearningTable

def update():
    for episode in range(100):
        # initial observation
        observation = env.reset()
        
        while True:
            # fresh env
            env.render()
            
            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            # updating q values
            RL.learn(str(observation), action, reward, str(observation_))
            
            # swap observation
            # For q-learning, we need to have both current state and next state
            # so we have not updated current state with next state
            # But after each q value update, we replace current state with next state
            observation = observation_

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()            

# If you want to run this RL, run the above.
# the below is the program to start your learning process
if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()     
            
            
            
            
            
            
            