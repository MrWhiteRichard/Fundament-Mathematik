# ---------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- #

def multi_armed_bandit_experiment(a, epsilon, steps):

    """

    input:
    a ......... array of mean values of normally distributed bandit rewards
    epsilon ... probability of exploratory action
    steps ..... number of bandit trials

    output:
    R_average ........... array of average reward up to time t (index)
    A_optimal_percent ... array of percent of optimal actions taken up to time t (index)

    """

    assert 0 <= epsilon <= 1

    k = len(a) # number of levers

    A_optimal = np.argmax(a) # actual optimal action

    bandit = lambda i: np.random.normal(a[i]) # bandit :)

    Q = np.zeros(k) # array of current value estimate per action (index)
    N = np.zeros(k) # array of number of times action (index) was taken

    R_average = np.zeros(steps)         # array of average reward up to time t (index)
    A_optimal_percent = np.zeros(steps) # array of percent of optimal actions taken up to time t (index)

    for t in range(1, steps):

        # in case there are multiple maximizing indices, the lowest one is selected
        A = np.random.randint(k) if np.random.uniform() <= epsilon else np.argmax(Q)
        R = bandit(A)

        N[A] += 1
        Q[A] += (R - Q[A]) / N[A]

        R_average[t]         = (R_average[t-1]         * (t-1) + R) / t
        A_optimal_percent[t] = (A_optimal_percent[t-1] * (t-1) + int(A == A_optimal)) / t

    return R_average, A_optimal_percent

# ---------------------------------------------------------------- #

epsilons = [0, 0.1, 0.5]

k = 10
steps = 1_000

a = np.random.normal(size = k) # array of standard normally distributed mean values fueling bandits

fig, axs = plt.subplots(2, 1)

for epsilon in epsilons:

    R_average, A_optimal_percent = multi_armed_bandit_experiment(a, epsilon, steps)

    label = r'$\varepsilon = ' + str(epsilon) + '$'

    axs[0].plot(range(steps), R_average,         label = label)
    axs[1].plot(range(steps), A_optimal_percent, label = label)

axs[0].set_xlabel('Steps')
axs[0].set_ylabel('Average reward')
axs[0].legend()

axs[1].set_xlabel('Steps')
axs[1].set_ylabel('% Optimal action')
axs[1].legend()

plt.show()

# ---------------------------------------------------------------- #
