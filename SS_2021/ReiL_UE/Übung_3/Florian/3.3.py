import numpy as np


### Evaluating the equiprobable policy

def policy_evaluation(pi, S, tau):

    V = np.zeros(10)    # state value array
    V[0] = 10
    V[9] = -5

    while True:
        delta = 0
        for s in S:
            v = V[s]
            V[s] = pi[s]*V[s-1] + (1 - pi[s])*V[s+1]
            delta = max(delta, np.abs(v - V[s]))
        if delta < tau:
            return V

def policy_improvement(pi, S, V):
    policy_stable = True
    for s in S:
        old_left_probability = pi[s]
        if V[s+1] > V[s-1]:
            pi[s] = 0
        else:
            pi[s] = 1
        if old_left_probability != pi[s]:
            policy_stable = False
    return pi, policy_stable


def policy_iteration(tau):
    pi = np.array([1/2]*10)
    S = np.arange(1,9)
    V = policy_evaluation(pi, S, tau)
    pi, policy_stable = policy_improvement(pi, S, V)
    print("Evaluation of random policy:", V)
    while policy_stable == False:
        V = policy_evaluation(pi, S, tau)
        pi, policy_stable = policy_improvement(pi, S, V)

    return pi, V



tau = 10e-6

pi, V = policy_iteration(tau)

print("V:", V)

print("pi:", pi)
