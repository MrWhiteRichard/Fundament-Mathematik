# ---------------------------------------------------------------- #

import gym
import random
import itertools
import os
import warnings

import numpy as np
import pandas as pd

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

class Parameterization:

    # should be specified for children: 'states' of 'state_action_pairs'
    feature_args = None

    def __init__(self, observation_space, action_space, feature_info):

        self.observation_space = observation_space
        self.action_space = action_space
        self.feature_info = feature_info

        self.observation_space_dim = get_space_dimension(self.observation_space)
        self.action_space_dim = get_space_dimension(self.action_space)

    @property
    def feature_amount(self):

        if self.feature_info['mode'] == 'polynomials':

            if self.feature_args == 'states':
                k = self.observation_space_dim

            elif self.feature_args == 'state_action_pairs':
                k = self.observation_space_dim + self.action_space_dim

            else:
                raise ValueError(f'args_mode = {self.feature_args}')

            n = self.feature_info['degree']

            return (n + 1) ** k

        else:
            raise NotImplementedError

    def features(self, state, action=None): # TODO: impolement Sutton&Barto's tiles3 instead

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

            if self.feature_args == 'states':

                k = self.observation_space_dim

                n = self.feature_info['degree']

                state = np.array(
                    get_element_list(self.observation_space, state)
                )

                assert len(state) == k

                c = np.array(
                    list(
                        itertools.product(range(n+1), repeat=k)
                    )
                )

                return np.array([
                    np.prod(state ** c_) for c_ in c
                ])

            elif self.feature_args == 'state_action_pairs':

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
                raise ValueError(f'args_mode = {self.feature_args}')


        else:
            raise NotImplementedError

    def close(self):
        pass

class PolicyParameterization(Parameterization):

    feature_args = 'state_action_pairs'

    def preference(self, state, action, theta):
        return theta @ self.features(state, action)

    def get_probabilities(self, state, theta, actions=None):

        """
        Reinforecment Learning (An Introduction) - second edition - Richard S. Sutton and Andrew G. Barto
        page 322
        exponential soft-max distribution, i.e. (13.2) & (13.3)
        """

        if actions is None:
            actions = get_space_list(self.action_space)

        preference_array = np.array([self.preference(state, action, theta) for action in actions])
        e_array = np.exp(preference_array)

        probabilities = e_array / np.sum(e_array)

        return probabilities

    def get_probability(self, state, theta, action):

        actions = get_space_list(self.action_space)
        probabilities = self.get_probabilities(state, theta, actions)

        index = actions.index(action)
        probability = probabilities[index]

        return probability

    def __call__(self, state, theta, action):
        return self.get_probability(state, theta, action)

    def get_action(self, state, theta):

        actions = get_space_list(self.action_space)
        probabilities = self.get_probabilities(state, theta, actions)

        return random.choices(population=actions, weights=probabilities)[0]

    def elegibility_vector(self, state, theta, action):

        """
        Reinforecment Learning (An Introduction) - second edition - Richard S. Sutton and Andrew G. Barto
        Exercise 13.3
        """

        actions = get_space_list(self.action_space)

        probabilities = self.get_probabilities(state, theta, actions)
        features_at_state = np.array([self.features(state, action) for action in actions])

        # (13.9): nabla ln pi(a|s, theta) = x(s, a) - sum_b pi(b|s, theta) x(s, b)
        return self.features(state, action) - probabilities @ features_at_state

class StateValueParameterization(Parameterization):

    feature_args = 'states'

    def __call__(self, state, w):
        return w @ self.features(state)

    def gradient(self, state, w):
        return self.features(state)

# ---------------------------------------------------------------- #

class StepSize:

    def __init__(self, expression):
        self.expression = str(expression)

    def __call__(self, n, a=None):

        self.step_size_current = None

        expression_exec = 'self.step_size_current = ' + self.expression.replace('n', str(n)).replace('a', str(a))
        assert str(None) not in expression_exec
        exec(expression_exec)

        assert self.step_size_current is not None
        return self.step_size_current

    def __str__(self):
        return self.expression

# ---------------------------------------------------------------- #

class Agent:

    """
        Reinforecment Learning (An Introduction) - second edition - Richard S. Sutton and Andrew G. Barto
        learning methods:
            # 1: page 328 ... REINFORCE: Monte-Carlo Policy-Gradient Control (episodic) for pi_*,
            # 2: page 330 ... REINFORCE with Baseline (episodic), for estimating pi_theta approx pi_*,
            # 3: page 332 ... One-step Actor-Critic (spisodic), for estimating pi_theta approx pi_*;
    """

    learning_methods = ['REINFORCE', 'REINFORCE with Baseline', 'One-step Actor-Critic']

    def __init__(
        self, env, gamma, feature_info, learning_method,
        alpha=None,
        alpha_theta=None, alpha_w=None):

        """
            Args:
                env ............... Environment
                gamma ............. discount rate
                feature_info ...... dictionary containing information about feature vectors
                learning_method ... in self.learning_methods

                alpha ............. step size

                alpha_theta ....... step size for policy's parameter vector
                alpha_w ........... step size for weights
        """

        self.env = env
        self.gamma = gamma

        # 1, 2, 3: Input: a differentiable policy parameterization pi(a|s, theta)
        self.pi = PolicyParameterization(
            self.env.observation_space,
            self.env.action_space,
            feature_info
        )

        # 2, 3: Input: a differentiable state-value function parameterization v_hat(s, w)
        self.v_hat = StateValueParameterization(
            self.env.observation_space,
            self.env.action_space,
            feature_info
        )

        self.learning_method = learning_method

        if self.learning_method == 'REINFORCE':

            # 1: Algorithm parameter: step sizes alpha > 0
            self.alpha = StepSize(alpha)

            # 1: Initialize poliy parameter theta in R^{d'} (e.g., to 0)
            d_prime = self.pi.feature_amount
            self.theta = np.zeros(d_prime)

        elif self.learning_method in ['REINFORCE with Baseline', 'One-step Actor-Critic']:

            # 2 / 3: Algorithm parameter / Parameter: step sizes alpha_theta > 0, alpha_w > 0
            self.alpha_theta = StepSize(alpha_theta)
            self.alpha_w = StepSize(alpha_w)

            # Initialize poliy parameter theta in R^{d'} and state-value weights w \in \R^d (e.g., to 0)

            d_prime = self.pi.feature_amount
            self.theta = np.zeros(d_prime)

            d = self.v_hat.feature_amount
            self.w = np.zeros(d)

        else:
            raise NotImplementedError

        # steps learned
        self.n = 0

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

    def learn_episode(self):

        if self.learning_method in ['REINFORCE', 'REINFORCE with Baseline']:

            # 1, 2: Generate an episode S_0, A_0, R_1, ..., S_{T-1}, A_{T-1}, R_T, following pi(.|., theta)
            S, A, R, T = self.generate_episode()

            # 1, 2: Loop for each step of the episode t = 0, 1, ..., T-1:
            for t in range(T):

                self.n += 1

                # 1, 2: G <- sum_{k=t+1}^T gamma^{k-t-1} R_k
                G = sum([
                    self.gamma ** (k-t-1) * R[k-1] # we are using R[k-1] instead of R[k] because, when indexing R, we start counting at 0
                    for k in range(t+1, T+1)
                ])

                if self.learning_method == 'REINFORCE':

                    assert self.alpha is not None

                    # 1: theta <- theta + alpha gamma^t G nabla ln pi(A_t|S_t, theta)
                    self.theta += self.alpha(self.n, A[t]) * self.gamma ** t * G * self.pi.elegibility_vector(S[t], self.theta, A[t])

                else: # self.learning_method == 'REINFORCE with Baseline':

                    assert self.alpha_theta is not None
                    assert self.alpha_w is not None

                    # 2: delta <- G - v_hat(S_t, w)
                    delta = G - self.v_hat(S[t], self.w)

                    # 2: w <- w + alpha_w delta nabla v_hat(S_t, w)
                    self.w += self.alpha_w(self.n, A[t]) * delta * self.v_hat.gradient(S[t], self.w)

                    # 2: theta <- theta + alpha_theta gamma^t delta nabla ln pi(A_t|S_t, theta)
                    self.theta += self.alpha_theta(self.n, A[t]) * self.gamma ** t * delta * self.pi.elegibility_vector(S[t], self.theta, A[t])

        elif self.learning_method == 'One-step Actor-Critic':
            
            # 3: Initialize S (first state of episode)
            S = self.env.reset()

            S_array = [S]
            A_array = []
            R_array = []
            T = 0

            # 3: I <- 1
            I = 1

            done = False

            # 3: Loop while S is not terminal (for each time step):
            while not done:

                self.n += 1

                # 3: A ~ pi(.|S, theta)
                A = self.pi.get_action(S, self.theta)
                action = A

                # 3: Take action A, observe S', R
                observation, reward, done, info = self.env.step(action)
                S_prime = observation
                R = reward

                A_array.append(action)
                R_array.append(reward)
                T += 1

                S_array.append(observation)

                # 3: delta <- R + gamma v_hat(S', w) - v_hat(S, w) (if S' is terminal, then v_hat(S', w) doteq 0)
                if not done:
                    delta = R + self.gamma * self.v_hat(S_prime, self.w) - self.v_hat(S, self.w)

                else:
                    delta = R - self.v_hat(S, self.w)

                # 3: w <- w + alpha_w delta nabla v_hat(S, w)
                self.w += self.alpha_w(self.n, A) * delta * self.v_hat.gradient(S, self.w)

                # 3: theta <- theta + alpha_theta I delta nabla ln pi(A|S, theta)
                self.theta += self.alpha_theta(self.n, A) * I * delta * self.pi.elegibility_vector(S, self.theta, A)

                # 3: I <- gamma I
                I *= self.gamma

                # 3: S <- S'
                S = S_prime
            
            S = S_array
            A = A_array
            R = R_array

        else:
            raise NotImplementedError

        return S, A, R, T

    def close(self):

        self.env.close()
        self.pi.close()
        self.v_hat.close()

    def reset(self):

        self.__init__(
            self.env, self.gamma, self.feature_info, self.learning_method,
            alpha=self.alpha,
            alpha_theta=self.alpha_theta, alpha_w=self.alpha_w
        )

# ---------------------------------------------------------------- #

env = gym.make('CartPole-v0')

# ---------------------------------------------------------------- #

from parameters import parameters_array

def measure(parameters):

    parameters = parameters_array[parameters_index]

    # -------------------------------- #
    # generate new data

    # instanciate agent
    if parameters['learning method'] == 'REINFORCE':
        ag = Agent(
            env, parameters['gamma'], parameters['feature info'], parameters['learning method'],
            alpha=parameters['alpha'],
        )

    elif parameters['learning method'] in ['REINFORCE with Baseline', 'One-step Actor-Critic']:
        ag = Agent(
            env, parameters['gamma'], parameters['feature info'], parameters['learning method'],
            alpha_theta=parameters['alpha_theta'], alpha_w=parameters['alpha_w'],
        )

    else:
        raise NotImplementedError

    total_reward_array = []

    for episode_number in range(parameters['episode number max']):

        S, A, R, T = ag.learn_episode()

        total_reward_array.append(
            sum(R)
        )

    # close agent
    ag.close()

    # -------------------------------- #
    # store new data in data base (.csv)

    file_name = f'df_{parameters_index}.csv'

    if file_name in os.listdir():
        
        # read and store old data in data frame
        runs = pd.read_csv(file_name, index_col=0)
        
        # append new data
        runs[int(runs.columns[-1]) + 1] = total_reward_array

    else:

        # create new data frame with new data
        runs = pd.DataFrame(total_reward_array)

    # create new data base (or "update" / replace the existing one)
    runs.to_csv(file_name)

    # -------------------------------- #

# ---------------------------------------------------------------- #
# Work Horse:

# -------------------------------- #

# index of `parameters_array`
parameters_index = None # please fill out

# how many runs should be learned additionally
runs = None # please fill out

# -------------------------------- #

for _ in range(runs):
    measure(parameters_index)

# -------------------------------- #

# ---------------------------------------------------------------- #
