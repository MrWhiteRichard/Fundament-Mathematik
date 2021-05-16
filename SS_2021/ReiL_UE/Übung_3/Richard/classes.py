# ---------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt

import random
import itertools

from functions import argsmax

# ---------------------------------------------------------------- #
# Exercise 37

class MDP:

    def __init__(self, gamma, epsilon, alpha):

        assert 0 <= gamma <= 1
        assert 0 <= epsilon <= 1
        assert 0 < alpha <= 1

        self.gamma = gamma
        self.epsilon = epsilon
        self.alpha = alpha

        self.episodes_learned = 0
        self.time_steps_observed = 0
        self.Q = self.Sarsa_initialize_Q()

    @property
    def states(self):
        pass

    @property
    def states_initial(self):
        return self.states

    @property
    def states_terminal(self):
        pass

    def actions(self, state):
        pass

    def observe_reward_and_new_state(self, state_old, action_old):
        pass

    def Sarsa_initialize_Q(self):

        # Q = {
        #     state: {
        #         action: np.random.random()
        #         for action in self.actions(state)
        #     }
        #     for state in self.states
        # }

        # for state_terminal in self.states_terminal:
        #     Q[state_terminal] = {
        #         action: 0
        #         for action in self.actions(state_terminal)
        #     }

        Q = {
            state: {
                action: 0
                for action in self.actions(state)
            }
            for state in self.states
        }

        return Q

    def Sarsa_initialize_S(self):
        return random.choice(self.states_initial)

    def Sarsa_choose_action(self, state):
        
        """
        Chosse $A$ from $S$ using policy derived from $Q$ (e.g. $\varepsilon$-greedy)
        """

        if not state in self.Q.keys():
            print(f'ERRER: {state} ist not a state!')

        if np.random.random() <= self.epsilon:
            return random.choice(
                self.actions(state)
            )
        else:
            return random.choice(
                argsmax(self.Q[state])
            )

    def pi(self, state):

        assert state in self.Q.keys()

        return random.choice(
            argsmax(self.Q[state])
        )

    def Sarsa_learn(self, episodes = 1):

        """
        Sarsa (on-policy TD control) for estimating $Q \approx q_\ast$
        page: 101
        """

        for episode in range(episodes):

            # print(f'learning episode {episode + 1} ...')

            S = self.Sarsa_initialize_S()
            A = self.Sarsa_choose_action(S)

            while not S in self.states_terminal:

                R, S_prime = self.observe_reward_and_new_state(S, A)
                A_prime = self.Sarsa_choose_action(S_prime)
                
                self.Q[S][A] += self.alpha * (R + self.gamma * self.Q[S_prime][A_prime] - self.Q[S][A])

                S = S_prime
                A = A_prime

                self.time_steps_observed += 1

        self.episodes_learned += episodes

    def generate_episode(self, state_action_initial = None, t_max = np.infty):

        if state_action_initial is None:
            
            state_initial = self.Sarsa_initialize_S()
            action_initial = self.Sarsa_choose_action(state_initial)

        else:
            state_initial, action_initial = state_action_initial

        S_array = [state_initial]
        A_array = [action_initial]
        R_array = [None]

        # print(S_array)

        t = 0

        while t < t_max:

            S = S_array[-1]
            A = A_array[-1]

            # print('old state:', S)
            # print('old action', A)

            R, S_prime = self.observe_reward_and_new_state(S, A)

            # print('observed reward', R)
            # print('observed state', S_prime)

            R_array.append(R)
            S_array.append(S_prime)

            if S_prime in self.states_terminal:
                # print('break')
                break

            A_prime = self.Sarsa_choose_action(S_prime)
            A_array.append(A_prime)
            # print('new action')
            # print()

            t += 1

        T = t

        return S_array, A_array, R_array, T

class WindyGridworldKingsMoves(MDP):

    def __init__(self,
        gamma, epsilon, alpha,
        width, height, wind_means, position_start, position_end
    ):

        assert width == len(wind_means)

        self.width = width
        self.height = height

        self.wind_means = wind_means

        self.position_start = position_start
        self.position_end = position_end

        super().__init__(gamma, epsilon, alpha)

    @property
    def size(self):
        return self.width, self.height

    @property
    def states(self):
        return list(
            itertools.product(
                range(self.width),
                range(self.height)
            )
        )

    @property
    def states_initial(self):
        return [self.position_start]

    @property
    def states_terminal(self):
        return [self.position_end]

    def actions(self, state):
        return list(
            action
            for action in itertools.product(
                range(-1, 1+1),
                range(-1, 1+1)
            )
            if action != (0, 0)
        )

    def wind(self, position):
        return self.wind_means[position]

    def observe_reward_and_new_state(self, state_old, action_old):

        reward = -1

        state_new = (
            max(0, min(self.width-1,  state_old[0] + action_old[0])),
            max(0, min(self.height-1, state_old[1] + action_old[1] + self.wind(state_old[0])))
        )

        return reward, state_new

    def plot(self, path, points, show_time = np.infty):

        fig_width = 8
        fig_height = 8 * self.height / self.width

        plt.figure(figsize = (fig_width, fig_height))

        plt.xlim(-1, self.width+1)
        plt.ylim(-1, self.height+1)

        x_array, y_array = np.array(path).T
        plt.plot(x_array, y_array, color = 'blue', zorder = -1)

        x_array, y_array = np.array(points).T
        plt.scatter(x_array, y_array, color = 'red', zorder = 1)

        if show_time == np.infty:
            plt.show()

        elif show_time != 0:

            plt.show(block = False)
            plt.pause(show_time)
            plt.close()

class WindyGridworldKingsMovesStationary(WindyGridworldKingsMoves):

    def actions(self, state):
        return list(
            action
            for action in itertools.product(
                range(-1, 1+1),
                range(-1, 1+1)
            )
            # if action != (0, 0)
        )

# ---------------------------------------------------------------- #
# Exercise 38

class WindyGridworldKingsMovesStochastic(WindyGridworldKingsMoves):

    def wind(self, position):
        return random.choice([self.wind_means[position] + offset for offset in range(-1, 1+1)])

# ---------------------------------------------------------------- #
