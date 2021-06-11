import gym
import numpy as np
import random
import time
from itertools import product

env = gym.make('CartPole-v0')


def x(state, action):
    # Fourier Basis order-1
    c_array = product([0,1], repeat = 5)
    return np.array([np.cos(np.dot(c,np.concatenate((state, [action])))) for c in c_array])

def pi(state, action, theta, env):
    normalize_factor = sum([np.exp(np.dot(theta, x(state,a))) for a in range(env.action_space.n)])
    return np.exp(np.dot(theta, x(state,action)))/normalize_factor

def choose_action(state, actions, theta, env):
    weights = [pi(state,action,theta, env) for action in actions]
    return random.choices(actions, weights = weights)[0]


def REINFORCE(alpha, max_episodes, env, dim):
    theta = np.zeros(dim)
    actions = [i for i in range(env.action_space.n)]
    episode_length_array = np.zeros(100)
    episode_length_array.fill(10)

    for i in range(max_episodes):
        done = False
        observation = env.reset()
        S = [observation]
        A = []
        R = [0]

        
        t = 0
        while not done:
            #print("Observation: ", observation)
            action = choose_action(observation, actions, theta, env)
            observation, reward, done, info = env.step(action)
            
            S.append(observation)
            A.append(action)
            R.append(reward)

            t += 1
            if done:
                episode_length_array[i%100] = t
                if i%20 == 0:
                    print(f"Episode {i} finished after {t} timesteps")
                    
                    print("Average length (last 100): ", np.mean(episode_length_array))
                break
        T = t
        
        for t in range(T):
            G = sum([R[k] for k in range(t+1,T+1)])
            gradient = x(S[t],A[t]) - sum([pi(S[t], action, theta, env)*x(S[t],action) for action in actions])
            #print("Gradient: ", gradient)
            theta += alpha*G*gradient
        
        #print("Theta: ", theta)
    
    return theta

theta = REINFORCE(2e-10, 500, env, 2**5)

observation = env.reset()
actions = [i for i in range(env.action_space.n)]
for t in range(100):
    env.render()
    action = choose_action(observation, actions, theta, env)
    observation, reward, done, info = env.step(action)
    if done:
        time.sleep(2)
        print("Episode finished after {} timesteps".format(t+1))
        break

env.close()