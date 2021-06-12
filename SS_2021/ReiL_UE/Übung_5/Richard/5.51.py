# ---------------------------------------------------------------- #

import gym
import random
import itertools
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- #

def get_space_list(space):

    """
    Converts gym `space`, constructed from `types`, to list `space_list`
    """

    # -------------------------------- #

    if '__iter__' in dir(space) and '__next__' in dir(space):
        return list(space)

    # -------------------------------- #

    types = [
        gym.spaces.multi_binary.MultiBinary,
        gym.spaces.discrete.Discrete,
        gym.spaces.multi_discrete.MultiDiscrete,
        gym.spaces.dict.Dict,
        gym.spaces.tuple.Tuple,
    ]

    if type(space) not in types:
        raise ValueError(f'input space {space} is not constructed from spaces of types:' + '\n' + str(types))

    # -------------------------------- #

    if type(space) is gym.spaces.multi_binary.MultiBinary:
        return [
            np.reshape(np.array(element), space.n)
            for element in itertools.product(
                range(2),
                repeat=np.prod(space.n)
            )
        ]

    if type(space) is gym.spaces.discrete.Discrete:
        return list(range(space.n))

    if type(space) is gym.spaces.multi_discrete.MultiDiscrete:
        return [
            np.array(element) for element in itertools.product(
                *[range(n) for n in space.nvec]
            )
        ]

    if type(space) is gym.spaces.dict.Dict:

        keys = space.spaces.keys()
        
        values_list = itertools.product(
            *[get_space_list(sub_space) for sub_space in space.spaces.values()]
        )

        return [
            {key: value for key, value in zip(keys, values)}
            for values in values_list
        ]

        return space_list

    if type(space) is gym.spaces.tuple.Tuple:
        return [
            list(element) for element in itertools.product(
                *[get_space_list(sub_space) for sub_space in space.spaces]
            )
        ]

    # -------------------------------- #

def get_space_dimension(space):

    types = [
        gym.spaces.box.Box,
        gym.spaces.multi_binary.MultiBinary,
        gym.spaces.discrete.Discrete,
        gym.spaces.multi_discrete.MultiDiscrete,
        gym.spaces.dict.Dict,
        gym.spaces.tuple.Tuple,
    ]

    if type(space) is gym.spaces.box.Box:
        return np.prod(space.shape)

    if type(space) is gym.spaces.multi_binary.MultiBinary:
        return np.prod(space.n)

    if type(space) is gym.spaces.discrete.Discrete:
        return 1

    if type(space) is gym.spaces.multi_discrete.MultiDiscrete:
        return len(space.nvec)

    if type(space) is gym.spaces.dict.Dict:
        return sum([get_space_dimension(sub_space) for sub_space in space.spaces.values()])

    if type(space) is gym.spaces.tuple.Tuple:
        return sum([get_space_dimension(sub_space) for sub_space in space.spaces])

def get_element_list(space, element):

    types = [
        gym.spaces.box.Box,
        gym.spaces.multi_binary.MultiBinary,
        gym.spaces.discrete.Discrete,
        gym.spaces.multi_discrete.MultiDiscrete,
        gym.spaces.dict.Dict,
        gym.spaces.tuple.Tuple,
    ]

    if type(space) is gym.spaces.box.Box:
        return list(element)

    if type(space) is gym.spaces.multi_binary.MultiBinary:
        return list(
            np.flatten(element)
        )

    if type(space) is gym.spaces.discrete.Discrete:
        return [element]

    if type(space) is gym.spaces.multi_discrete.MultiDiscrete:
        return list(
            np.flatten(element)
        )

    if type(space) is gym.spaces.dict.Dict:

        element_list = []

        for element_component in element.values():
            element_list += get_element_list(element_component)

        return element_list

    if type(space) is gym.spaces.tuple.Tuple:

        element_list = []

        for element_component in element:
            element_list += get_element_list(element_component)

        return element_list
        
# ---------------------------------------------------------------- #

class Policy:

    def __init__(self, observation_space, action_space, feature_info):

        self.observation_space = observation_space
        self.action_space = action_space
        self.feature_info = feature_info

        self.observation_space_dim = get_space_dimension(self.observation_space)
        self.action_space_dim = get_space_dimension(self.action_space)

        # get feature amount
        if self.feature_info['mode'] == 'polynomials':

            k = self.observation_space_dim + self.action_space_dim
            n = self.feature_info['degree']

            self.feature_info['amount'] = (n + 1) ** k

    def features(self, state, action): # TODO: impolement Sutton&Barto's tiles3 instead

        """
        Reinforecment Learning (An Introduction) - second edition - Richard S. Sutton and Andrew G. Barto
        9.5 Feature Construction for Linear Methods
        9.5.1 Polynomials <- implemented
        9.5.2 Fourier Basis
        9.5.3 Coarse Coding
        9.5.4 Tile Coding
        9.5.5 Radial Basis Functions
        """

        if self.feature_info['mode'] == 'polynomials':

            k = self.observation_space_dim + self.action_space_dim
            n = self.feature_info['degree']

            state_action_pair = np.array(
                get_element_list(self.observation_space, state) + get_element_list(self.action_space, action)
            )

            assert len(state_action_pair) == k

            c = np.array(
                list(
                    itertools.product(range(n+1), repeat=k)
                )
            )

            return np.array([
                np.prod(state_action_pair ** c_) for c_ in c
            ])

        else:
            raise NotImplementedError

    def h(self, state, action, theta):
        d_prime = len(theta)
        return theta @ self.features(state, action)

    def get_probabilities(self, state, theta, actions=None):

        """
        Reinforecment Learning (An Introduction) - second edition - Richard S. Sutton and Andrew G. Barto
        page 322
        exponential soft-max distribution, i.e. (13.2) & (13.3)
        """

        if actions is None:
            actions = get_space_list(self.action_space)

        h_array = np.array([self.h(state, action, theta) for action in actions])
        e_array = np.exp(h_array)

        probabilities = e_array / np.sum(e_array)

        return probabilities

    def get_probability(self, state, theta, action):

        actions = get_space_list(self.action_space)
        probabilities = self.get_probabilities(state, theta, actions)

        index = actions.index(action)
        probability = probabilities[index]

        return probability

    def get_action(self, state, theta):

        actions = get_space_list(self.action_space)
        probabilities = self.get_probabilities(state, theta, actions)

        return random.choices(population=actions, weights=probabilities)[0]

    def elegibility_vector(self, action, state, theta):

        """
        Reinforecment Learning (An Introduction) - second edition - Richard S. Sutton and Andrew G. Barto
        Exercise 13.3
        """

        d_prime = len(theta)

        actions = get_space_list(self.action_space)

        probabilities = self.get_probabilities(state, theta, actions)
        features_at_state = np.array([self.features(state, action) for action in actions])

        return self.features(state, action) - probabilities @ features_at_state

    def close(self):
        del self.feature_info['amount']

# ---------------------------------------------------------------- #

class Agent:

    def __init__(self, env, gamma, alpha, feature_info):

        """
            Args:
                env ............ Environment
                gamma .......... discount rate
                alpha .......... step size
                feature_info ... dictionary containing information about feature vectors
        """

        self.env = env
        self.gamma = gamma

        # Input: a differentiable policy parameterization pi(a|s, theta)
        self.pi = Policy(
            self.env.observation_space,
            self.env.action_space,
            feature_info
        )

        # Algorithm parameter: step size alpha > 0
        self.alpha = alpha

        # Initialize poliy parameter theta in R^{d'} (e.g., to 0)
        d_prime = self.pi.feature_info['amount']
        self.theta = np.zeros(d_prime)

    def generate_episode(self):

        S = [self.env.reset()]
        A = []
        R = []
        T = 0

        done = False

        while not done:

            action = self.pi.get_action(self.env.state, self.theta)
            observation, reward, done, info = self.env.step(action)

            A.append(action)
            R.append(reward)
            T += 1

            S.append(observation)

            self.env.state = observation

        return S, A, R, T

    def REINFORCE_episode(self):

        """
        Reinforecment Learning (An Introduction) - second edition - Richard S. Sutton and Andrew G. Barto
        page 328
        REINFORCE: Monte-Carlo Policy-Gradient Control (episodic) for pi_ast
        """

        # Generate an episode S_0, A_0, R_1, ..., S_{T-1}, A_{T-1}, R_T, following pi(.|., theta)
        S, A, R, T = self.generate_episode()

        # Loop for each step of the episode t = 0, 1, ..., T-1:
        for t in range(T):

            # G <- sum_{k=t+1}^T gamma^{k-t-1} R_k
            G = sum([
                self.gamma ** (k-t-1) * R[k-1] # we are using R[k-1] instead of R[k] because, when indexing R, we start counting at 0
                for k in range(t+1, T+1)
            ])

            # theta <- theta + alpha gamma^t G nabla ln pi(A_t|S_t, theta)
            self.theta += self.alpha * self.gamma ** t * G * self.pi.elegibility_vector(A[t], S[t], self.theta)

    def average_episode_length(self, sample_episode_number=1):

        T_array = []
        
        for _ in range(sample_episode_number):
            S, A, R, T = ag.generate_episode()
            T_array.append(T)

        return np.average(
            np.array(T_array)
        )

    def close(self):
        self.env.close()
        self.pi.close()

# ---------------------------------------------------------------- #

env = gym.make('CartPole-v0')

# ---------------------------------------------------------------- #

def test_1():
    env.reset()
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample()) # take a random action
    env.close()

# test_1()

def test_2():
    episodes = 10
    for episode in range(1, episodes+1):
        env.reset()
        done = False
        score = 0

        while not done:
            env.render()
            action = env.action_space.sample()
            n_state, reward, done, info = env.step(action)
            score += reward

        print(f'Episode: {episode}' + '\n' + f'Score: {score}' + '\n')

# test_2()

# ---------------------------------------------------------------- #

def measure(parameters):

    # -------------------------------- #
    # generate new data

    ag = Agent(
        env,
        parameters['gamma'],
        parameters['alpha'],
        parameters['feature_info']
    )

    total_reward_array = []

    for episode_number in range(parameters['episode_number_max']):

        S, A, R, T = ag.generate_episode()

        total_reward_array.append(
            sum(R)
        )

        ag.REINFORCE_episode()

    # -------------------------------- #

    ag.close()

    # read and store old data in data frame
    # append new data
    if (file_name := f'{parameters}.csv'.replace(':', ' =')) in os.listdir():
        runs = pd.read_csv(file_name, index_col=0)
        runs[int(runs.columns[-1]) + 1] = total_reward_array
    else:
        runs = pd.DataFrame(total_reward_array)

    # update data file
    runs.to_csv(file_name)

# ---------------------------------------------------------------- #

parameters = {
    'gamma': 0.9,
    'alpha': 0.1,
    'feature_info': {'mode': 'polynomials', 'degree': 1},
    'episode_number_max': 100
}

for _ in range(50):
    measure(parameters)

# ---------------------------------------------------------------- #
