import numpy as np
import time


### Evaluating the equiprobable policy

def policy_evaluation(pi, S, R, tau):

    V = np.array([0 for s in S], dtype = float)    # state value array
    counter = 0
    while True:
        delta = 0
        for s in S:
            v = V[s]
            if 0 < s & s < 9:
                V[s] = pi[s]*(V[s-1] + R[s-1]) + (1 - pi[s])*(V[s+1] + R[s+1])
            delta = max(delta, np.abs(v - V[s]))
        counter += 1
        if delta < tau:
            return V, counter

def policy_improvement(pi, S, R, V):
    policy_stable = True
    for s in S:
        old_left_probability = pi[s]
        if 0 < s & s < 9:
            if V[s+1] + R[s+1] > V[s-1] + R[s-1]:
                pi[s] = 0
            else:
                pi[s] = 1
            if old_left_probability != pi[s]:
                policy_stable = False

    return pi, policy_stable


def policy_iteration(tau, R):
    pi = np.array([1/2]*10)
    S = np.arange(10)
    V, iteration_counter = policy_evaluation(pi, S, R, tau)
    pi, policy_stable = policy_improvement(pi, S, R, V)
    random_evaluation = V
    random_num_iterations = iteration_counter
    counter = 0
    while policy_stable == False:
        V,_ = policy_evaluation(pi, S, R, tau)
        pi, policy_stable = policy_improvement(pi, S, R, V)
        counter += 1

    return pi, V, counter, random_evaluation, random_num_iterations


#tolerance
tau = 10e-6

# Reward array
R = np.zeros(10)
R[0] = 10
R[9] = -5

tic = time.time()
pi, V, counter, random_evaluation, random_num_iterations = policy_iteration(tau, R)
toc = time.time()

print("Evaluation of random policy:", np.round(random_evaluation,2))
print("Number of iterations:", random_num_iterations)

print("Time:", toc - tic)
print("V:", V)

print("policy:", pi)

print("Number of policy improvements:", counter)
