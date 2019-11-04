# -*- coding: utf-8 -*-
"""
Reinforcement learning maze example.

Red rectangle:      explorer.
Black rectangles:   hells       [reward = -1].
Yellow bin circle:  paradise    [reward = +1].
All other states:   ground      [reward = 0].

This script is the environment part of this example. The RL is in RL_brain.
py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/

YUKI COMMENT
- action is not determined in this file
- 

"""
import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
UNIT = 40 # pixels
MAZE_H = 4 # grid height
MAZE_W = 4 # grid width

class Maze(tk.Tk, object):
    # initialization
    def __init__(self):
        super(Maze, self).__init__()
        
        # Define action space
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')
        
        # What is this?
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()
        
    # method to create environment by drawing with tkinter
    def _build_maze(self):
        
        # rk.Canvas makes maze environment which will pop up when you run
        self.canvas = tk.Canvas(self, bg='white',
                                height=MAZE_H * UNIT,
                                width=MAZE_W * UNIT)
        
        # create grids
        # Just drawing 3 horizontal and vertical lines each
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_H * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)
    
        # create origin
        # Specifying the center coordinate of our start point
        origin = np.array([20, 20])
        
        # hell
        # right one at 2nd row 3rd col
        hell1_center = origin + np.array([UNIT * 2, UNIT])
        # Each state box is 40 by 40 so draw 30 by 30 box inside representing a hole.
        self.hell1 = self.canvas.create_rectangle(
                hell1_center[0] - 15, hell1_center[1] - 15,
                hell1_center[0] + 15, hell1_center[1] + 15,
                fill='black')
        
        # hell
        # left one at 3rd row 2nd col
        hell2_center = origin + np.array([UNIT, UNIT * 2])
        self.hell2 = self.canvas.create_rectangle(
                hell2_center[0] - 15, hell2_center[1] - 15,
                hell2_center[0] + 15, hell2_center[1] + 15,
                fill='black')
        
        # create oval
        # drawing yellow circle which is our goal state
        oval_center = origin + UNIT * 2
        self.oval = self.canvas.create_oval(
                oval_center[0] - 15, oval_center[1] - 15,
                oval_center[0] + 15, oval_center[1] + 15,
                fill='yellow')
        
        # create red rect
        # drawing our start point
        self.rect = self.canvas.create_rectangle(
                origin[0] - 15, origin[1] - 15,
                origin[0] + 15, origin[1] + 15,
                fill='red')
        
        # pack all
        self.canvas.pack()
        
    # I guess reset put red rectangle back to start point 
    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        self.rect = self.canvas.create_rectangle(
                origin[0] - 15, origin[1] - 15,
                origin[0] + 15, origin[1] + 15,
                fill='red')
        # return observation
        return self.canvas.coords(self.rect)
        
    # this allows agent to move to the next state
    def step(self, action):
        # I guess getting current state of agent. rect is agent
        s = self.canvas.coords(self.rect)
        # in base_action, 1st element is horizontal movement, and 2nd element is vertical movement
        base_action = np.array([0, 0])
        # Where is the action set?
        if action == 0: # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1: # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2: # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3: # left
            if s[0] > UNIT:
                base_action[0] -= UNIT
        
        # rect is agent. This makes actual movement
        self.canvas.move(self.rect, base_action[0], base_action[1]) # move agent
        
        # getting coordinante of after movement, that is next state
        s_ = self.canvas.coords(self.rect) # next state
        
        # reward function
        # if next state is oval state, then it means you reached goal, so you give agent a reward
        if s_ == self.canvas.coords(self.oval):
            reward = 1
            done = True
        # if next state is hellm then it means you dropped into the hole, so you give agent a punishment -1 reward
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2)]:
            reward = -1
            done = True
        # otherwise, you don't give agent any reward or punishment
        else:
            reward = 0
            done = False
        
        return s_, reward, done
    
    def render(self):
        time.sleep(0.1)
        self.update()
        
def update():
    # what is t?
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 1
            s, r, done = env.step(a)
            # done has both goal and hell
            if done:
                break

# I don't understand this, what is dot after
if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()
        
        
        
        
        