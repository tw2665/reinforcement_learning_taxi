# AML-Project

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
  
  
  
Original taxi env:

  * Description: There are four designated locations in the grid world indicated by R(ed), G(reen), Y(ellow), and B(lue). When the episode starts, the taxi starts off at a random square and the passenger is at a random location. The taxi drives to the passenger's location, picks up the passenger, drives to the passenger's destination (another one of the four specified locations), and then drops off the passenger. Once the passenger is dropped off, the episode ends.

  * Observations: There are 500 discrete states since there are 25 taxi positions, 5 possible locations of the passenger (including the case when the passenger is in the taxi), and 4 destination locations. 
  
  
 Potential updates:
 
 * Add penaties and rewards. 
 * Increase canvas size based on needs.
 * Change number of destination or pick-up locations.
 * Limit the direction of turns under some circumstances.

## Workflow of using TF-agent to perform Deep Q-learning

1. Make environment by tf_py_environment
2. Make network by q_network
3. Make agent by dqn_agent (network is set inside agent)
4. Make replay buffer
5. Set environment, agent, and replay buffer inside driver
6. Perform training by getting trajectory from replay buffer and feed the trajectory into train method from agent object 

## Terminology

Time step:

* Time step is a function taking input of action and returns next observation (aka state) and reward from that action. 

Policy:
 
* Policy is a strategy that an agent take.
* The goal of RL is to learn the best policy.
* Policy is a function which has input as state (or observation) and returns output as action.
* We use policy to make an agent decide which action to take in a given state.
* In practice, policy is a set of values in a look-up table

Driver:

* Driver is used to train agent.
* People say that we use driver to collect experience from environment.
* It is a object to run a loop of executing a policy in an environment.
* The result of drive will be stored in Trajectory.

Trajectory:

* Trajectory is a tuple containing data from training.
* It includes observation (aka state) from environment, action taken by policy, reward, current and next step.
* It is like experience.

Replay buffer:

* Replay buffer is an object to store trajectory.
* It gets subset of trajectory to replay a sequence of the subset or sample.
* It requires data_spec, which we can get from agent.collect_data_spec.

## DQN

* DQN is Deep Q Network. It's neural network that has states as input and produce a vector of action values as output.
* Selects and evaluate an action, which results in overoptimitic value estimates.

## DDQN

* DDQN is Double Deep Q Network, which can reduce overestimation and can deliver better performance. It says even DQN sometimes overestimates the values of actions. It says on the Atari domain, DDQN delivered a better result than DQN.

## SAC

* SAC is Soft Actor-Critic algorithm
* Handles discrete and continuous action spaces, off-policy training, combine actor network and critic network.
* In practice, it largely eliminates the need for per-task hyperparameter tuning.
* actor-critic architecture separately has policy and value function, efficient off-policy formulation because it resues previously collected data, entropy maximization for stability and exploration.

