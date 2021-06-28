import gym
import numpy as np
import random
import time
from itertools import product

env = gym.make('CartPole-v0')


def x(state, action):
    # Fourier Basis order-1
    c_array = product([0,1], repeat = 5)
    features = np.array([np.cos(np.dot(c,np.concatenate((state, [action])))) for c in c_array])

    # Polynomial Basis order-1
    # c_array = product([0,1], repeat = 5)
    # features = np.array([np.prod(np.concatenate((state, [action + 1]))**np.array(c)) for c in c_array])
    return features

def pi(state, theta, env):
    # print(theta)
    # print(np.exp(theta @ x(state,0)))
    # print(np.exp(theta @ x(state,1)))
    p_array = np.array([np.exp(np.dot(theta, x(state,action))) for action in range(env.action_space.n)])
    return p_array/np.sum(p_array)

def choose_action(state, actions, theta, env):
    weights = pi(state, theta, env)
    #print(weights)
    return random.choices(population = actions, weights = weights)[0]


def REINFORCE(alpha, gamma, max_episodes, env, dim):
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

        
        T = 0
        while not done:
            #print("Observation: ", observation)
            action = choose_action(observation, actions, theta, env)
            observation, reward, done, info = env.step(action)
            
            S.append(observation)
            A.append(action)
            R.append(reward)

            T += 1
            if done:
                episode_length_array[i%100] = T
                if i%20 == 0:
                    print(f"Episode {i} finished after {T} timesteps")
                    
                    if T < 100:
                        mean = np.mean(episode_length_array[:T])
                    else:
                        mean = np.mean(episode_length_array)
                    print("Average length (last 100): ", mean)
                break
        for t in range(T):
            G = sum([gamma**(k-t-1)*R[k] for k in range(t+1,T+1)])
            probabilities = pi(S[t], theta, env)
            features = np.array([x(S[t],action) for action in actions])
            gradient = x(S[t],A[t]) - probabilities @ features
            theta += alpha*gamma**t*(G-10)*gradient
        
        #print("Theta: ", theta)
    
    print(episode_length_array)
    return theta

def REINFORCE_BASELINE(alpha, gamma, max_episodes, env, dim):

    pass


theta = REINFORCE(0.01, 1, 500, env, 2**5)
print(theta)
observation = env.reset()
actions = [i for i in range(env.action_space.n)]
for t in range(100):
    env.render()
    action = choose_action(observation, actions, theta, env)
    observation, reward, done, info = env.step(action)
    if done:
        time.sleep(1)
        print("Episode finished after {} timesteps".format(t+1))
        break



env.close()