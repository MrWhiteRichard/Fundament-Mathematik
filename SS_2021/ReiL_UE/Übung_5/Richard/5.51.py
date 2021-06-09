# ---------------------------------------------------------------- #

import gym
import random

import numpy as np

# ---------------------------------------------------------------- #

class Policy:

    metadata = {'features.modes': ['polynomials']}

    def __init__(self, action_space, feature_mode='polynomials'):
        self.action_space = action_space

    def features(self, d_prime, state, action): # TODO: impolement Sutton&Barto's tiles3 instead

        """
        Reinforecment Learning (An Introduction) - second edition - Richard S. Sutton and Andrew G. Barto
        9.5 Feature Construction for Linear Methods
        9.5.1 Polynomials <- implemented
        9.5.2 Fourier Basis
        9.5.3 Coarse Coding
        9.5.4 Tiel Roding
        9.5.5 Radial Basis Functions
        """

        if self.feature_mode == 'polynomials':

            s = np.array(state)
            k = len(s)
            c = np.array([np.arange(k) for i in range(d_prime)])

            return np.array([
                np.prod(s ** c[i]) for i in range(d_prime)
            ])

        else:
            raise NotImplementedError

    def h(self, state, action, theta):
        d_prime = len(theta)
        return theta @ self.features(d_prime, state, action)

    def get_probabilities(self, state, theta, actions=None):

        """
        Reinforecment Learning (An Introduction) - second edition - Richard S. Sutton and Andrew G. Barto
        page 322
        exponential soft-max distribution, i.e. (13.2) & (13.3)
        """

        if actions is None:
            actions = list(self.action_space)

        h_array = np.array([self.h(state, action, theta) for action in actions])
        e_array = np.exp(h_array)

        probabilities = e_array / np.sum(e_array)

        return probabilities

    def get_probability(self, state, theta, action):

        actions = list(self.action_space)
        probabilities = self.get_probabilities(state, theta, actions)

        index = actions.index(action)
        probability = probabilities[index]

        return probability

    def get_action(self, state, theta):

        actions = list(self.action_space)
        probabilities = self.get_probabilities(state, theta, actions)

        return random.choices(population=actions, weights=probabilities)[0]

    def elegibility_vector(self, action, state, theta):

        """
        Reinforecment Learning (An Introduction) - second edition - Richard S. Sutton and Andrew G. Barto
        Exercise 13.3
        """
        actions = list(self.action_space)

        probabilities = self.get_probabilities(state, theta, actions)
        features_at_state = np.array([self.features(state, action) for action in actions])

        return self.features(state, action) - probabilities @ features_at_state

# ---------------------------------------------------------------- #

class Agent:

    def __init__(self, env, d_prime, alpha, pi=None, theta=None):

        self.env = env

        # Input: a differentiable policy parameterization pi(a|s, theta)
        if pi is not None:
            self.pi = pi
        else:
            pi = Policy(self.env.action_space)

        # Algorithm parameter: step size alpha > 0
        self.alpha = alpha

        # Initialize poliy parameter theta in R^{d'} (e.g., to 0)
        if theta is not None:
            self.theta = theta
        else:
            self.theta = np.zeros(d_prime)

    def generate_episode(self):

        S = [self.env.reset()]
        A = []
        R = []
        T = 0

        done = False

        while not done:

            self.env.render() # debug

            action = self.pi.get_action(S[-1], self.theta)
            observation, reward, done, info = self.env.step(action)

            A.append(action)
            R.append(reward)
            T += 1

            S.append(observation)

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
