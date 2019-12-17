# Reinforcement Learning on OpenAI Gym Taxi

This is a group project of Advanced Machine Learning course at Columbia University MA in Statistics 2019 Fall.

## Member   
* Ethan Li
* Tianchen Wang
* [Yuki Kitayama](https://github.com/yukikitayama)
* Liwei Zhang
  
## Introduction

In this project, we borrow the below Taxi environment from [OpenAI Gym](https://gym.openai.com/) and perform reinforcement learning to solve our task. The yellow box is a taxi, and this color means the taxi does not have a passenger inside. The pink letter suggests a passenger is waiting the taxi, and this passenger wants to go to the destination of a blue letter. Our task is to let the taxi to go to the passenger location, pick it up, take it to the destination, and successfully drop it off. So, in reinforcement learning setting, the taxi is our agent.

![taxi_env][1]

## Results

Here briefly presents the current results we have. Please see our [report](https://github.com/tw2665/AML-Project-/blob/master/documents/GR5242_Final_Project_Report.pdf) and codes in this project for the detail. We implemented Deep Q Network and Double Deep Q Network and obtained the following rewards.

**DQN**
![dqn_reward][2]
**DDQN**
![ddqn_reward][3]

## Discussion
* Learning is not
* The environment is simple, so maybe we can increase the size of environmet, put some penalty obstacles inside, or add some tasks.

## Methodology
The below is the set of methodology that this project has covered. DQN and DDQN are implemented by coding with gym and TensorFlow as well as [TF-Agents](https://github.com/tensorflow/agents)
* Q-Learning
* Deep Q Network (DQN)
* Double Deep Q Network (DDQN)

## Environment
* There are 500 discrete states since there are 25 taxi positions, 5 possible locations of the passenger (including the case when the passenger is in the taxi), and 4 destination locations.

## Creating a new environnment in gym
We researched how to modify the existing environment in OpenAI Gym. This would be used for your further analysis.
* https://github.com/openai/gym/blob/master/docs/creating-environments.md
* https://github.com/openai/gym-soccer

## Terminology
* Time step
    * Time step is a function taking input of action and returns next observation (aka state) and reward from that action. 
* Policy
    * Policy is a strategy that an agent take. The goal of RL is to learn the best policy.
    * Policy is a function which has input as state (or observation) and returns output as action.
    * We use policy to make an agent decide which action to take in a given state. In practice, policy is a set of values in a look-up table
* Driver
    * Driver is used to train agent. People say that we use driver to collect experience from environment.
    * It is a object to run a loop of executing a policy in an environment. The result of drive will be stored in Trajectory.
* Trajectory
    * Trajectory is a tuple containing data from training. It includes observation (aka state) from environment, action taken by policy, reward, current and next step.
* Replay buffer
    * Replay buffer is an object to store trajectory. It gets subset of trajectory to replay a sequence of the subset or sample.
    * It requires data_spec, which we can get from agent.collect_data_spec.
* DQN
    * Deep Q Network. It's neural network that has states as input and produce a vector of action values as output.
    * Selects and evaluate an action, which results in overoptimitic value estimates.
* DDQN
    * Double Deep Q Network, which can reduce overestimation and can deliver better performance. It says even DQN sometimes overestimates the values of actions. It says on the Atari domain, DDQN delivered a better result than DQN.
* SAC
    * Soft Actor-Critic algorithm. It handles discrete and continuous action spaces, off-policy training, combine actor network and critic network.
    * In practice, it largely eliminates the need for per-task hyperparameter tuning.
    * actor-critic architecture separately has policy and value function, efficient off-policy formulation because it resues previously collected data, entropy maximization for stability and exploration.

[1]:https://github.com/tw2665/AML-Project-/blob/master/images/taxi_env.png
[2]:https://github.com/tw2665/AML-Project-/blob/master/images/dqn_reward.png
[3]:https://github.com/tw2665/AML-Project-/blob/master/images/ddqn_reward.png
