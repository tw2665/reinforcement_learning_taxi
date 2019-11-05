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
  
## OpenAi gym tutorial.

### How to create a new environnment in gym.

https://github.com/openai/gym/blob/master/docs/creating-environments.md

https://github.com/openai/gym-soccer

How to modify Taxi environment
  * Open taxi.py. It contains map, so we modify this map, and adjust number of states, columns, rows, and so on.
  * 
  
  
  
Original taxi env
  * Description: There are four designated locations in the grid world indicated by R(ed), G(reen), Y(ellow), and B(lue). When the episode starts, the taxi starts off at a random square and the passenger is at a random location. The taxi drives to the passenger's location, picks up the passenger, drives to the passenger's destination (another one of the four specified locations), and then drops off the passenger. Once the passenger is dropped off, the episode ends.

  * Observations: There are 500 discrete states since there are 25 taxi positions, 5 possible locations of the passenger (including the case when the passenger is in the taxi), and 4 destination locations. 
  
  
  

