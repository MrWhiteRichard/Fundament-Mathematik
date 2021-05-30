# ---------------------------------------------------------------- #

import random
import numpy as np
import matplotlib.pyplot as plt

from gym import Env
from gym.spaces.space import Space

from collections import defaultdict
from fractions import Fraction
from time import time

from outsource import *

# ---------------------------------------------------------------- #

class BackendEnv(Env):

    def __init__(self, gamma, alpha, n, epsilon, default_action_value=0):

        self.gamma = gamma
        self.alpha = alpha
        self.n = n
        self.epsilon = epsilon

        self.Q = defaultdict(
            lambda: defaultdict(
                lambda: default_action_value
            )
        )

        self.Model = defaultdict(dict)

        self.pi = Policy(self.action_space)

    def sarsa_episode(self):

        states = [None] * (self.n + 1)
        actions = [None] * (self.n + 1)
        rewards = [None] * (self.n + 1)

        # Initialilze and store S_0 != terminal
        states[0] = self.reset()

        # Select and store an action A_0 ~ b(.|S_0)
        actions[0] = self.pi.get_action(self.state)

        # T <- infty
        T = np.infty

        t = 0

        # Loop for t = 0, 1, 2, ... :
        while True:

            # If t < T, then:
            if t < T:

                # Take action A_t
                # Observe and store the next reward as R_{t+1} and the next state as S_{t+1}
                observation, reward, done, _ = self.step(actions[t % (self.n + 1)])
                states[(t + 1) % (self.n + 1)] = observation
                rewards[(t + 1) % (self.n + 1)] = reward

                # If S_{t+1} is terminal, then:
                if done:

                    # T <- t + 1
                    T = t + 1

                # else:
                else:

                    # Select and store an action A_{t+1} ~ b(.|S_{t+1})
                    self.state = np.copy(states[(t + 1) % (self.n + 1)])
                    actions[(t + 1) % (self.n + 1)] = self.pi.get_action(self.state)

            # tau <- t - n + 1 (tau is the time whose estimate is being updated)
            tau = t - self.n + 1

            # If tau >= 0:
            if tau >= 0:

                # G <- sum_{i=tau+1}^{min(tau+n,T)} gamma^{i-tau-1} R_i
                G = sum([
                    self.gamma ** (i - tau - 1) * rewards[i % (self.n + 1)]
                    for i in range(
                        tau + 1, min(tau + self.n, T) + 1
                    )
                ])

                # If tau + n < T, then G <- G + gamma^n Q(S_{tau+n}, A_{tau+n})
                if tau + self.n < T:
                    G += self.gamma ** self.n * self.Q[str(states[(tau + self.n) % (self.n + 1)])][str(actions[(tau + self.n) % (self.n + 1)])]

                # Q(S_tau, A_tau) <- Q(S_tau, A_tau) + alpha [G - Q(S_tau, A_tau)]
                error = G - self.Q[str(states[tau % (self.n + 1)])][str(actions[tau % (self.n + 1)])]
                self.Q[str(states[tau % (self.n + 1)])][str(actions[tau % (self.n + 1)])] += self.alpha * error

                # If pi is being learned, then ensure that pi(.|S_tau) is epsilon-greedy wrt Q
                self.pi = Policy(
                    self.action_space,
                    epsilon=self.epsilon,
                    Q=self.Q
                )


            # Until tau = T - 1
            if tau == T - 1:
                break

            t += 1

        return T

    def dyna_q_episode(self):

        self.reset()

        T = 0
        done = False

        while not done:

            T += 1
        
            # S <- current (nonterminal) state
            S = self.state

            # A <- epsilon-greedy(S, Q)
            if random.random() <= self.epsilon:
                A = self.action_space.sample()
            else:
                A = random.choice(
                    argsmax({
                        A_prime: self.Q[str(S)][str(A_prime)]
                        for A_prime in self.action_space
                    })
                )

            # Take action A; observe resultant reward, R, and state, S_prime
            observation, reward, done, info = self.step(A)

            S_prime = observation
            R = reward

            # Q(S, A) <- Q(S, A) + alpha [R + gamma max_a Q(S_prime, a) - Q(S, A)]
            error = R + self.gamma * max([self.Q[str(S_prime)][str(a)] for a in self.action_space]) - self.Q[str(S)][str(A)]
            self.Q[str(S)][str(A)] += self.alpha * error

            self.state = np.copy(S_prime)

            # -------------------------------- #

            # Model(S, A) <- R, S_prime (assuming deterministic environment)
            self.Model[str(S)][str(A)] = (R, np.copy(S_prime))

            # Loop repeat n times
            for _ in range(self.n):

                # S <- random previously observed state
                str_S = random.choice(
                    list(
                        self.Model.keys()
                    )
                )

                # A <- random action previously taken in S
                str_A = random.choice(
                    list(
                        self.Model[str_S].keys()
                    )
                )

                # R, S_prime <- Model(S, A)
                R, S_prime = self.Model[str_S][str_A]

                # Q(S, A) <- Q(S, A) + alpha [R + gamma max_a Q(S_prime, a) - Q(S, A)]
                error = R + self.gamma * max([self.Q[str(S_prime)][str(a)] for a in self.action_space]) - self.Q[str_S][str_A]
                self.Q[str_S][str_A] += self.alpha * error

        return T

# ---------------------------------------------------------------- #

class DynaMazeSpace(Space):

    def __init__(self, data=None):
        self.data = [] if data is None else data

    @property
    def size(self):
        return len(self.data)

    def sample(self):
        return random.choice(self.data)

    def contains(self, x):
        return str(x) in [str(_) for _ in self.data]

    def index(self, value):
        return self.data.index(value)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __len__(self):
        return self.size

class RandomWalkActionSpace(DynaMazeSpace):

    def __init__(self):
        self.data = ['up', 'down', 'right', 'left']

class RandomWalkObservationSpace(DynaMazeSpace):

    def __init__(self, data, initial, terminal):

        self.data = data
        self.initial = DynaMazeSpace(initial)
        self.terminal = DynaMazeSpace(terminal)

    @property
    def non_terminal(self):
        return DynaMazeSpace([
            state for state in self if tuple(state) not in [tuple(state_terminal) for state_terminal in self.terminal]
        ])

class DynaMazeEnv(Env):

    action_space = RandomWalkActionSpace()

    def __init__(self, filename):

        image = plt.imread(filename)

        data = []
        initial = []
        terminal = []

        n, m, _ = image.shape

        self.shape = (m, n)

        for i in range(n):
            for j in range(m):

                position = np.array([j, n-i-1])

                if not np.array_equal(image[i, j], np.zeros(3)):
                    data.append(position)

                    if np.array_equal(image[i, j], np.array([1, 0, 0])):
                        initial.append(position)

                    if np.array_equal(image[i, j], np.array([0, 1, 0])):
                        terminal.append(position)

        self.observation_space = RandomWalkObservationSpace(data, initial, terminal)

        self.reset()

    def step(self, action):

        assert action in self.action_space, f'{action} invalid action, not in {self.action_space.data}'

        shifts = {
            'up':    np.array([ 0,  1]),
            'down':  np.array([ 0, -1]),
            'right': np.array([ 1,  0]),
            'left':  np.array([-1,  0])
        }

        info = {}

        if (dummy := self.state + shifts[action]) not in self.observation_space:
            observation = self.state
            info['crash'] = True
        else:
            observation = dummy
            info['crash'] = False

        done = (observation in self.observation_space.terminal)
        reward = int(done)

        return observation, reward, done, info

    def reset(self):
        self.state = random.choice(self.observation_space.initial)
        return self.state

    def render(self, mode='rgb_array'):

        if mode == 'rgb_array':
            
            render = np.zeros((*self.shape, 3))

            for i, j in self.observation_space:
                render[i, j] = np.ones(3)

            for i, j in self.observation_space.initial:
                render[i, j] = np.array([1, 0, 0])

            for i, j in self.observation_space.terminal:
                render[i, j] = np.array([0, 1, 0])

            i, j = self.state
            render[i, j] = np.array([0, 0, 1])

            render = np.rot90(render, axes=(0, 1))

            return render

        else:
            super().render(mode=mode) # just raise an exception

# ---------------------------------------------------------------- #

class MyDynaMazeEnv(DynaMazeEnv, BackendEnv):

    def __init__(
        self,
        filename,
        gamma, alpha, n, epsilon, default_action_value=0
    ):

        DynaMazeEnv.__init__(self, filename)
        BackendEnv.__init__(self, gamma, alpha, n, epsilon, default_action_value)

# ---------------------------------------------------------------- #

def test_1():

    """
    Testing: .step-method by selecting random actions via .action_space.sample-method
    """

    env = DynaMazeEnv('map.png')

    done = False

    t = 0

    while not done:

        action = env.action_space.sample()
        observation, _, done, info = env.step(action)

        env.state = observation

        t += 1

    print(t)

# test_1()

# ---------------------------------------------------------------- #

def test_2(algorithm, n_array=[1], run_number_max=1):

    """
    algorithm:
        Dyna Q:
            Try to reproduce Figure 8.2 on page 165.
        Sarsa:
            Then apply a multi-step algorithm to this problem.
    """

    time_start_global = time()

    filename = 'map.png'

    gamma = 0.95
    alpha = 0.1
    n_array = [0, 5, 50] if algorithm == 'Dyna Q' else n_array
    epsilon = 0.1

    runs = []

    run_number_max = 30 if algorithm == 'Dyna Q' else run_number_max
    for run_number in range(run_number_max):

        print(f'run number: {run_number + 1} / {run_number_max}')
        print()

        run = {n: [] for n in n_array}

        for n in n_array:

            print(f'n: {n}')

            time_start_local = time()

            env = MyDynaMazeEnv(filename, gamma, alpha, n, epsilon)

            episode_number_max = 50
            for episode_number in range(episode_number_max):

                print(f'episode number: {episode_number+1} / {episode_number_max}')

                if algorithm == 'Dyna Q':
                    run[n].append(
                        env.dyna_q_episode()
                    )

                elif algorithm == 'Sarsa':
                    run[n].append(
                        env.sarsa_episode()
                    )

                else:
                    raise NotImplementedError

            print('time passed ...')
            print(f'local:  {round(time() - time_start_local,  2)}')
            print(f'global: {round(time() - time_start_global, 2)}')
            print()

        runs.append(run)

    steps_per_episode_dict = {
        n: [
            np.average([run[n][episode_number] for run in runs])
            for episode_number in range(episode_number_max)
        ]
        for n in n_array
    }

    plt.figure()

    start = 1
    for n, steps_per_episode in steps_per_episode_dict.items():

        label = f'{n} planning steps' if algorithm == 'Dyna Q' else f'{n} steps'
        plt.plot(range(start, episode_number_max), steps_per_episode[start:], label=label)

    plt.suptitle(
        algorithm + '\n' + r'$\gamma = $' + str(gamma) + ', ' + r'$\alpha = $' + str(alpha) + ', ' + r'$\epsilon = $' + str(epsilon) + '\n'
    )

    plt.legend()
    plt.xlabel('Episodes')
    plt.ylabel('Steps per episode')

    plt.show()

# test_2('Dyna Q')

n_array = [1, 25, 50]
run_number_max = 10
test_2('Sarsa', n_array, run_number_max)

# ---------------------------------------------------------------- #
