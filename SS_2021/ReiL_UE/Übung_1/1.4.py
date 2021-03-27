# ---------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- #

def multi_armed_bandit_run(a, epsilon, steps):

    """

    input:
    a ......... array of mean values of normally distributed bandit rewards
    epsilon ... probability of exploratory action
    steps ..... number of bandit trials

    output:
    R ... array of rewards received at time t (index)
    A ... array of actions taken at time t (index)

    """

    assert 0 <= epsilon <= 1
    k = len(a) # number of levers
    bandit = lambda i: np.random.normal(a[i]) # bandit :)

    Q = np.zeros(k) # array of current value estimate per action (index)
    N = np.zeros(k) # array of number of times action (index) was taken

    R = np.zeros(steps) # array of rewards received at time t (index)
    A = np.zeros(steps, dtype = int) # array of actions taken at time t (index)

    for t in range(1, steps):

        # in case there are multiple maximizing indices, the lowest one is selected
        A[t] = np.random.randint(k) if np.random.uniform() <= epsilon else np.argmax(Q)
        R[t] = bandit(A[t])

        N[A[t]] += 1
        Q[A[t]] += (R[t] - Q[A[t]]) / N[A[t]]

    return R, A

def multi_armed_bandit_experiment(a, epsilon, steps, runs):

    """

    input:
    a ......... array of mean values of normally distributed bandit rewards
    epsilon ... probability of exploratory action
    steps ..... number of bandit trials per run
    steps ..... number of bandit runs

    output:
    R_average ........... array of average reward up to time t (index)
    A_optimal_percent ... array of percent of optimal actions taken up to time t (index)

    """

    assert 0 <= epsilon <= 1

    k = len(a) # number of levers
    A_optimal = np.argmax(a) # actual optimal action

    R = np.zeros((runs, steps))
    A = np.zeros((runs, steps), dtype = int)

    for r in range(runs):

        print(f'epsilon = {epsilon}, run = {r}')
        R[r], A[r] = multi_armed_bandit_run(a, epsilon, steps)

    # array of average reward up to time t (index)
    R_average = np.array([
        np.average(R[:, t])
        for t in range(steps)
    ])
    
    # array of percent of optimal actions taken up to time t (index)
    A_optimal_percent = np.array([
        np.count_nonzero(A[:, t] == A_optimal) / runs
        for t in range(steps)
    ])

    return R_average, A_optimal_percent

# ---------------------------------------------------------------- #

epsilons = [0, 0.1, 0.5]

k = 10
steps = 1_000
runs = 1_000

a = np.random.normal(size = k) # array of standard normally distributed mean values fueling bandits

fig, axs = plt.subplots(2, 1)

for epsilon in epsilons:

    R_average, A_optimal_percent = multi_armed_bandit_experiment(a, epsilon, steps, runs)

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
