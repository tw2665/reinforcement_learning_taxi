# AML-Project-

Advanced Machine Learning Project

Topic
  * Reinforcement learning
  
Member
  * Ethan Li
  * Tianchen Wang
  * Yuki Kitayama
  * Liwei Zhang
  
General idea about reinforcement learning

  * Make environment (state space) with reward and actions that an agent take (action space), set a goal that the agent wants to achieve, and estimate the optimal path by model or algorithm. 
  
  * Brainstorming 
    * Campus walk
     * Make a miniature Columbia campus. Agent starts from a building, buy and take out a lunch from a food truck or deli, and find an optimal location to eat it.
     
  * Use open environment from OpenAI
    * The Open ai Gym contains multiple environments that we can work on.Such as invader and Black Jack.  So maybe we can take a look at the website and find something interesting to work on.https://gym.openai.com/envs/#atari
    
(Write your idea) 
(Explain your idea) 
Challenging part
  * Mapping the environment and specify all the possible moves (This equals to making Q table if you apply Q-learning).
Theoretical things
  * Q-learning
  * Markov decision process
    * Model for decision making, which you can use when some part is random, but you know some part.
    * A Markov reward process with a decision factor in it.
  * SARSA (State Action Reward next State and next Action)
Very similar to Q-learning, but the difference is that Q-learning takes argmax, but SARSA doesn’t.

Resource (Reference)
  * Reinforcement Learning - With Open AI, TensorFlow and Keras Using Python; Abhishek Nandy, Manisha Biswas; apress
  
  * Reinforcement Q-learning from scratch in python with OpenAI gym
  https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/
  
  
  * Reinforcement learning methods and tutorials (Github repo)
  https://www.kaggle.com/charel/learn-by-example-reinforcement-learning-with-gym (A kaggle example)
  https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow
  
  * 莫煩 python 教學 (Youtube about RL)
  https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
  
OpenAi gym tutorial.

How to create a new environnment in gym.

https://github.com/openai/gym/blob/master/docs/creating-environments.md
https://github.com/openai/gym-soccer

