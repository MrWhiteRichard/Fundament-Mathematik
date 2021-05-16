# ---------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt

import itertools

from PIL import Image
from outsource import argsmax

# ---------------------------------------------------------------- #

class Racetrack:

    # using:
    # On-policy first-visit MC control (for $\varepsilon$-soft policies), estimates $\pi \approx \pi_\ast$
    # page: 101

    colors = {
        'values': {
            'border': (0, 0, 0),
            'track': (255, 255, 255),
            'starting line': (255, 0, 0),
            'finish line': (0, 255, 0)
        },
        'names': {
            'border': 'black',
            'track': 'white',
            'starting line': 'red',
            'finish line': 'green'
        }
    }

    speed_limit = 2 # should be: 4

    actions_all = list(itertools.product(range(-1, 1+1), range(-1, 1+1)))

    velocities_all = list(
        itertools.product(
            range(speed_limit+1),
            range(speed_limit+1)
        )
    )

    def __init__(self, file_name, gamma = 0.9, epsilon = 0.1):

        self.file_name = file_name

        # In order to avoid computational cost, these should not be a @property
        self.image = Image.open(self.file_name)
        self.layout = self.get_layout()

        self.gamma = gamma
        self.epsilon = epsilon

        self.pi, self.Q, self.Returns = self.monte_carlo_initialize()

    @property
    def size(self):
        return self.image.size

    @property
    def width(self):
        return self.image.size[0]

    @property
    def height(self):
        return self.image.size[1]

    def get_layout(self):

        layout = {
            'border': [],
            'track': [],
            'starting line': [],
            'finish line': []
        }

        for x in range(self.width):
            for y in range(self.height):

                color_current = self.image.getpixel((x, y))

                for layout_part_name, layout_part_color in Racetrack.colors['values'].items():
                    if color_current == layout_part_color:
                        layout[layout_part_name].append(
                            (x, self.height - 1 - y)
                        )
        return layout

    def plot(self, extra = None, show_time = np.infty):

        plt.figure(figsize = (5, 5))

        for layout_part_name, layout_part_color in Racetrack.colors['names'].items():

            x_array, y_array = np.array(self.layout[layout_part_name]).T

            plt.scatter(
                x_array, y_array, color = layout_part_color, marker = 's'
            )

            if not extra is None:
                plt.scatter(*extra, color = 'blue', marker = 's')

        if show_time == np.infty:
            plt.show()

        elif show_time != 0:
            plt.show(block = False)
            plt.pause(show_time)
            plt.close()

    def view_trajectory_plot(
        self,
        S, A,
        crash_counter, steps_before_last_crash,
        show_time = np.infty,
        show_log = False
    ):

        S_safe = S[-steps_before_last_crash[crash_counter]:]
        # A_safe = A[-steps_before_last_crash[crash_counter]:]

        self.plot(
            extra = np.array(S_safe)[:, 0, :].T,
            show_time = show_time
        )

    def view_trajectory_log(
        self,
        S, A,
        crash_counter, steps_before_last_crash
    ):

        S_safe = S[-steps_before_last_crash[crash_counter]:]
        A_safe = A[-steps_before_last_crash[crash_counter]:]

        for state, action in zip(S_safe, A_safe):
            print(state)
            print(action)
            print()

        print('#', '-'*64, '#', '\n')

    @property
    def positions_all(self):
        return self.layout['track'] + self.layout['starting line'] + self.layout['finish line']

    @property
    def states_all(self):
        return list(
                itertools.product(
                    self.positions_all,
                    Racetrack.velocities_all
                )
            )

    def actions(self, state):
        return [
            action
            for action in Racetrack.actions_all
            if (velocity := (state[1][0] + action[0], state[1][1] + action[1])) in Racetrack.velocities_all and velocity != (0, 0)
        ]

    def monte_carlo_initialize(self):

        # We are not using
        # "an arbitrary $\varepsilon$-soft policy",
        # but rather the "equi probable" policy
        pi = {
            state: {
                action: 1 / len(self.actions(state))
                for action in self.actions(state)
            }
            for state in self.states_all
        }

        Q = {
            state: {
                action: np.random.random()
                for action in self.actions(state)
            }
            for state in self.states_all
        }

        Returns = {
            state: {
                action: []
                for action in self.actions(state)
            }
            for state in self.states_all
        }

        return pi, Q, Returns

    def position_initial(self):

        choose_from = self.layout['starting line']
        index = np.random.choice(
            range(len(choose_from))
        )

        return choose_from[index]

    velocity_initial = (0, 0)

    def action_from_policy(self, state):

        actions, probabilities = zip(*self.pi[state].items())
        
        index = 0

        while True:

            index = np.random.choice(
                range(len(actions)), p = probabilities
            )

            velocity_new = (state[1][0] + actions[index][0], state[1][1] + actions[index][1])

            if velocity_new in Racetrack.velocities_all and velocity_new != (0, 0):
                return actions[index]

    def monte_carlo_generate_episode(self, show_time = 0, show_log = False):
        
        """
        Not
        "Generate an episode folliwing $\pi$: $S_0, A_0, R_1, \dots, S_{T-1}, A_{T-1}, R_T$",
        but rather
        Generate an episode folliwing $\pi$: $S_0, A_0, R_0, \dots, S_{T-1}, A_{T-1}, R_{T-1}$.
        """

        S = [
            (
                self.position_initial(),
                Racetrack.velocity_initial
            )
        ]

        A = [
            self.action_from_policy(S[-1])
        ]

        R = [] # starts indexing at 0

        crash_counter = 0
        steps_before_last_crash = [0]

        while True: # crash_counter < 16:

            state_old = S[-1]
            action_old = A[-1]

            position_new = (
                state_old[0][0] + state_old[1][0],
                state_old[0][1] + state_old[1][1]
            )
            velocity_new = (
                state_old[1][0] + action_old[0],
                state_old[1][1] + action_old[1]
            )

            if position_new in self.layout['finish line']:
                R.append(0)
                break

            else:

                R.append(-1)

                if position_new not in self.layout['starting line'] + self.layout['track']:

                    if show_log:

                        print(f'Crash (number {crash_counter+1})!', '\n')
                        self.view_trajectory_log(
                            S, A,
                            crash_counter, steps_before_last_crash
                        )

                    if show_time != 0:
                        self.view_trajectory_plot(
                            S, A,
                            crash_counter, steps_before_last_crash,
                            show_time = show_time
                        )

                    crash_counter += 1
                    steps_before_last_crash.append(0)

                    position_new = self.position_initial()
                    velocity_new = Racetrack.velocity_initial

                else:

                    steps_before_last_crash[crash_counter] += 1

                state_new = (position_new, velocity_new)
                S.append(state_new)

                action_new = self.action_from_policy(state_new)
                A.append(action_new)
            
        assert len(S) == len(A) == len(R)

        T = len(S)

        return S, A, R, T, crash_counter, steps_before_last_crash

    def monte_carlo_learn_episodes(self, episodes = 1):

        for episode in range(episodes):

            S, A, R, T, _, _ = self.monte_carlo_generate_episode()

            G = 0

            for t in range(T-1, 0-1, -1):

                G = self.gamma * G + R[t]

                S_ = S[t]
                A_ = A[t]

                if not (S_, A_) in zip(S[:t], A[:t]):

                    actions = self.actions(S_)
                    number_of_actions = len(actions)

                    self.Returns[S_][A_].append(G)
                    self.Q[S_][A_] = np.average(self.Returns[S_][A_])

                    choose_from = argsmax(self.Q[S_])
                    index = np.random.choice(
                        range(len(choose_from))
                    )
                    A_star = choose_from[index]

                    self.pi[S_] = {
                        action: self.epsilon / number_of_actions
                        for action in actions
                    }
                    self.pi[S_][A_star] += 1 - self.epsilon

# ---------------------------------------------------------------- #

# -------------------------------- #

def drive(learned_episodes, plot_final = False, show_time = 0, show_log = False):

    print(f'learned episodes: {learned_episodes}', '\n')

    S, A, R, T, crash_counter, steps_before_last_crash = my_racetrack.monte_carlo_generate_episode(show_time = show_time, show_log = show_log)

    print(f'crashed {crash_counter} time(s) before reaching finish line', '\n')

    if plot_final:

        print('plotting last trajectory ...', '\n')
        my_racetrack.view_trajectory_plot(S, A, crash_counter, steps_before_last_crash)

    print('#', '-'*32,'#', '\n')

    return crash_counter

# -------------------------------- #

my_racetrack = Racetrack('map_2.png')

learned_episodes = 0

drive(learned_episodes, plot_final = True, show_time = 0.25, show_log = True)

episodes = 10_000
print(f'learning {episodes} episodes ...', '\n')
my_racetrack.monte_carlo_learn_episodes(episodes)
learned_episodes += episodes

crash_counters = []

drives = 32
for _ in range(drives):
    crash_counters.append(
        drive(learned_episodes, show_time = 1, show_log = True)
    )

print(f'average crashes, from {drives} drives, after having learned {learned_episodes} episodes: {np.average(crash_counters)}', '\n')

print('one more "for the road" ...', '\n')
drive(learned_episodes, plot_final = True, show_time = 1, show_log = True)

# -------------------------------- #

# ---------------------------------------------------------------- #
