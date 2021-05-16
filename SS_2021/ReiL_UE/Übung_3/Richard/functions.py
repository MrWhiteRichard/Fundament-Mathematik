# ---------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt

import time

# ---------------------------------------------------------------- #

def argsmax(A):

    if type(A) == dict:
        maximum = max(A.values())
        return [i for i, a in A.items() if a == maximum]

    if type(A) == list:
        maximum = max(A)
        return [i for i, a in enumerate(A) if a == maximum]

    return None

# ---------------------------------------------------------------- #

def test(class_name, sample_size = 1_000, episodes_learn = 10, sample_size_peak = None, episodes_learned_max = 1_000):

    if sample_size_peak is None:
        sample_size_peak = sample_size * 10

    # -------------------------------- #

    gamma = 0.9
    epsilon = 0.1
    alpha = 0.5

    width = 10
    height = 7

    wind_means = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

    position_start = (0, 3)
    position_end = (7, 3)

    my_windy_gridworld = class_name(
        gamma, epsilon, alpha,
        width, height, wind_means, position_start, position_end
    )

    # -------------------------------- #

    T_averages_array = []

    while my_windy_gridworld.episodes_learned < episodes_learned_max:

        # -------------------------------- #

        print(f'measuring average episode length with a sample of size {sample_size} ...')
        time_start = time.time()

        T_array = []

        for _ in range(sample_size):

            _, _, _, T = my_windy_gridworld.generate_episode()
            T_array.append(T)

        time_end = time.time()
        print(f'took {time_end - time_start} seconds', '\n')

        # -------------------------------- #

        T_averages_array.append(
            np.average(T_array)
        )

        # -------------------------------- #

        print(f'learning {episodes_learn} episodes ...')
        time_start = time.time()

        my_windy_gridworld.Sarsa_learn(episodes_learn)
        my_windy_gridworld.episodes_learned += episodes_learn

        time_end = time.time()
        print(f'took {time_end - time_start} seconds', '\n')

        # -------------------------------- #

        if my_windy_gridworld.episodes_learned % 100 == 0:

            print(f'learned {my_windy_gridworld.episodes_learned} episodes so far')
            print('plotting a sample path')
            print()
            
            S, _, _, _ = my_windy_gridworld.generate_episode()
            my_windy_gridworld.plot(
                S,
                [my_windy_gridworld.position_start, my_windy_gridworld.position_end, S[-1]],
                show_time = 0.5
            )

        # -------------------------------- #

    # -------------------------------- #

    plt.figure()

    x = range(len(T_averages_array))
    y = T_averages_array

    plt.semilogy(x, y)

    plt.xlabel(f'episodes times {episodes_learn}')
    plt.ylabel('average episode length')
    plt.show()

    # -------------------------------- #

    print(f'conducting another measurment at peak performance, i.e. {my_windy_gridworld.episodes_learned} episodes leaned, using {sample_size_peak} samples ...')

    T_array = []

    for _ in range(sample_size_peak):

        _, _, _, T = my_windy_gridworld.generate_episode()
        T_array.append(T)

    print(f'result: {np.average(T_array)} time steps per episode (on average)')

    # -------------------------------- #

# ---------------------------------------------------------------- #
