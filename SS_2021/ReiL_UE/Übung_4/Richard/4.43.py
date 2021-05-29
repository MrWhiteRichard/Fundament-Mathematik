# ---------------------------------------------------------------- #

# import gym
# env = gym.make('CartPole-v0')
# for i_episode in range(20):
#     observation = env.reset()
#     for t in range(100):
#         env.render()
#         print(observation)
#         action = env.action_space.sample()
#         observation, reward, done, info = env.step(action)
#         if done:
#             print("Episode finished after {} timesteps".format(t+1))
#             break
# env.close()

# ---------------------------------------------------------------- #

import random
import numpy as np
import matplotlib.pyplot as plt

from gym import Env
from gym.spaces.space import Space

from collections import defaultdict
from fractions import Fraction

# ---------------------------------------------------------------- #

class Policy(object):

    def __init__(self, action_space, data=None):

        self.action_space = action_space
        self.data = data

    def set_data(self, data=None):

        if data is None:
            self.reset()
        else:
            self.__data = data

    def get_data(self):
        return self.__data

    data = property(get_data, set_data)

    def reset(self):
        self.data = defaultdict(
            lambda: {
                str(action): 1 / self.action_space.size
                for action in self.action_space
            }
        )

    def __getitem__(self, key):

        if type(key) is not tuple:
            state = key
            return self.data[str(state)]
        else:
            state, action = key
            return self.data[str(state)][str(action)]

    def __setitem__(self, key, value):

        if type(key) is not tuple:
            state = key
            self.data[str(state)] = value
        else:
            state, action = key
            self.data[str(state)][str(action)] = value

    def get_action(self, state):

        actions, probabilities = zip(*self[state].items())
        action = random.choices(population=actions, weights=probabilities)[0]

        return action

    def __str__(self):
        return str(self.__data)

# ---------------------------------------------------------------- #

class TDEnv(Env):

    def __init__(self, gamma, alpha, n, pi, mode='dynamic', default_value=None):


        self.gamma = gamma
        self.alpha = alpha
        self.n = n

        self.V = defaultdict(float) if default_value is None else defaultdict(lambda: default_value)
        self.pi = pi

        assert mode in ['dynamic', 'static']
        self.mode = mode

    def TD_episode(self):

        states = [None] * (self.n + 1)
        rewards = [None] * (self.n + 1)
        errors = [None] * self.n

        states[0] = self.reset()
        T = np.infty
        t = 0

        while True:

            if t < T:

                self.state = states[t % (self.n + 1)]
                action = self.pi.get_action(self.state)

                observation, reward, done, _ = self.step(action)

                states[(t + 1) % (self.n + 1)] = observation
                rewards[(t + 1) % (self.n + 1)] = reward

                if done:
                    T = t + 1

                errors[t % self.n] = rewards[(t + 1) % (self.n + 1)] + self.gamma * self.V[str(states[(t + 1) % (self.n + 1)])] - self.V[str(states[t % (self.n + 1)])]

            tau = t - self.n + 1

            if tau >= 0:

                if self.mode == 'dynamic':

                    G = sum([
                        self.gamma ** (i - tau - 1) * rewards[i % (self.n + 1)]
                        for i in range(
                            tau + 1, min(tau + self.n, T) + 1
                        )
                    ])

                    if tau + self.n < T:
                        G += self.gamma ** self.n * self.V[str(states[(tau + self.n) % (self.n + 1)])]

                    error = G - self.V[str(states[tau % (self.n + 1)])]

                elif self.mode == 'static':
                    error = sum([
                        self.gamma ** (k-tau) * errors[k % self.n]
                        for k in range(
                            tau, min(T-1, tau+self.n-1) + 1
                        )
                    ])

                self.V[str(states[tau % (self.n + 1)])] += self.alpha * error

            if tau == T - 1:
                break

            t += 1

# ---------------------------------------------------------------- #

class RandomWalkSpace(Space):

    data = []
    size = len(data)

    def sample(self):
        return random.choice(self.data)

    def contains(self, x):
        return x in self.data

    def index(self, value):
        return self.data.index(value)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self):
        return self.size

class RandomWalkActionSpace(RandomWalkSpace):

    data = ['left', 'right']
    size = len(data)

class RandomWalkObservationSpace(RandomWalkSpace):

    data = [-np.infty] + ['A', 'B', 'C', 'D', 'E'] + [np.infty]
    size = len(data)

class RandomWalkObservationSpaceInitial(RandomWalkSpace):

    data = [RandomWalkObservationSpace.data[RandomWalkObservationSpace.size // 2]]
    size = len(data)

class RandomWalkObservationSpaceTerminal(RandomWalkSpace):

    data = [-np.infty, np.infty]
    size = len(data)

class RandomWalkObservationSpaceNonTerminal(RandomWalkSpace):

    data = [state for state in RandomWalkObservationSpace.data if state not in RandomWalkObservationSpaceTerminal.data]
    size = len(data)

class RandomWalkEnv(Env):

    def __init__(self):

        self.action_space = RandomWalkActionSpace()
        self.observation_space = RandomWalkObservationSpace()
        self.observation_space_initial = RandomWalkObservationSpaceInitial()
        self.observation_space_terminal = RandomWalkObservationSpaceTerminal()
        self.observation_space_non_terminal = RandomWalkObservationSpaceNonTerminal()

        self.reset()

    def step(self, action):

        assert action in self.action_space
        assert self.state not in self.observation_space_terminal

        index = self.observation_space.index(self.state)

        shift = {'left': -1, 'right': 1}
        observation = self.observation_space[index + shift[action]]

        if self.state == self.observation_space[-2] and observation == self.observation_space[-1]:
            reward = 1
        else:
            reward = 0

        done = (observation in self.observation_space_terminal)

        info = {}

        return observation, reward, done, info

    def reset(self):

        self.state = random.choice(self.observation_space_initial)
        return self.state

# ---------------------------------------------------------------- #

class MyRandomWalkEnv(RandomWalkEnv, TDEnv):

    def __init__(self, gamma, alpha, n, pi=None, mode='dynamic', default_value=None):

        RandomWalkEnv.__init__(self)

        if pi is None:
            pi = Policy(self.action_space)

        TDEnv.__init__(self, gamma, alpha, n, pi, mode, default_value)

# ---------------------------------------------------------------- #

def test_1():

    gamma = 0.9
    alpha = 0.1
    n = 4

    env = MyRandomWalkEnv(gamma, alpha, n)

    observations = [env.reset()]
    actions = []
    rewards = []

    done = False
    while not done:

        action = env.pi.get_action(env.state) # env.action_space.sample()
        observation, reward, done, _ = env.step(action)

        env.state = observation

        observations.append(observation)
        actions.append(action)
        rewards.append(reward)

    print("Episode finished after {} timesteps".format(len(observations)), '...')
    for observation, action, reward in zip(observations, actions, rewards):
        print(observation, action, reward)
    print()

    print(env.pi)
    print()

    env.close()

# test_1()

# ---------------------------------------------------------------- #

def test_2():

    gamma = 1
    alpha = 0.1
    n = 4
    mode = 'static'

    env = MyRandomWalkEnv(gamma, alpha, n, mode=mode)

    for _ in range(100_000):
        env.TD_episode()

    for i, key in enumerate(env.observation_space_non_terminal):
        value = env.V[key]
        print(f'{key}: {Fraction(value).limit_denominator(6)}')
        print(f'error: {abs(value - (i+1) / 6)}')

# test_2()

# ---------------------------------------------------------------- #

def test_3(gamma, alpha, n):

    default_value = 0.5

    runs = 100

    envs_dynamic = [MyRandomWalkEnv(gamma, alpha, n, mode='dynamic', default_value=default_value) for _ in range(runs)]
    envs_static = [MyRandomWalkEnv(gamma, alpha, n, mode='static', default_value=default_value) for _ in range(runs)]

    V = {'A': 1/6, 'B': 2/6, 'C': 3/6, 'D': 4/6, 'E': 5/6}

    RMS_averages_dynamic = []
    RMS_averages_static = []

    episode_max = 100

    for episode in range(episode_max):

        RMSs_dynamic = []
        RMSs_static = []

        for env_dynamic, env_static in zip(envs_dynamic, envs_static):

            env_dynamic.TD_episode()
            env_static.TD_episode()

            errors_dynamic = np.array([
                V[state] - env_dynamic.V[state]
                for state in V.keys()
            ])

            RMSs_dynamic.append(
                np.sqrt(
                    np.average(errors_dynamic ** 2)
                )
            )

            errors_static = np.array([
                V[state] - env_static.V[state]
                for state in V.keys()
            ])

            RMSs_static.append(
                np.sqrt(
                    np.average(errors_static ** 2)
                )
            )
        
        RMS_averages_dynamic.append(np.average(RMSs_dynamic))
        RMS_averages_static.append(np.average(RMSs_static))

    plt.figure()

    plt.plot(range(episode_max), RMS_averages_dynamic, label='dynamic')
    plt.plot(range(episode_max), RMS_averages_static, label='static')

    plt.suptitle(r'$\gamma = $' + str(gamma) + ', ' + r'$\alpha = $' + str(alpha) + ', ' + r'$n = $' + str(n))
    plt.xlabel('Walks / Episodes')
    plt.ylabel('Empirical RMS error, averaged over 100 runs')
    plt.legend()

    plt.show()

gamma = 0.9
alpha = 0.05
n = 4

test_3(gamma, alpha, n)

# ---------------------------------------------------------------- #
