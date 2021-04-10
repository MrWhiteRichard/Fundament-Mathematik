import random
import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)

action_values = [random.gauss(0,1) for x in range(10)]

max_reward = max(action_values)
optimal_action = action_values.index(max_reward)

expected_random_reward = sum(action_values)/10


print(action_values)
fig, axs = plt.subplots(2)
axs[0].tick_params(axis='both', which='major', labelsize=20)
axs[1].tick_params(axis='both', which='major', labelsize=20)

for epsilon in [1,0.5,0.1,0.01,0]:

    reward_array = np.zeros((1000,1000))
    action_array = np.zeros((1000,1000))
    for i in range(1000):
        action_value_estimates = [0 for x in range(10)]

        action_numbers = [0 for x in range(10)]
        for j in range(1000):
            r = random.uniform(0,1)
            if r < epsilon:
                action = random.randrange(0,10)
            else:
                indices = [i for i, x in enumerate(action_value_estimates) if x == max(action_value_estimates)]
                action = random.choice(indices)

            reward = random.gauss(action_values[action], 1)

            action_numbers[action] += 1
            action_value_estimates[action] += (reward - action_value_estimates[action])/action_numbers[action]

            reward_array[i,j] = reward
            action_array[i,j] = action


    reward_averages = [np.sum(reward_array[:,j])/1000 for j in range(1000)]


    optimal_action_percentages = [np.count_nonzero(action_array[:,j] == optimal_action)/1000 for j in range(1000)]

    axs[0].plot(range(1000), reward_averages, label = r"$\epsilon = {}$".format(epsilon), linestyle = "dashed")
    axs[1].plot(range(1000), optimal_action_percentages, label = r"$\epsilon = {}$".format(epsilon))

plt.grid(True)


axs[0].plot(range(1000), [max_reward for i in range(1000)], label = "optimum", color = "red")
axs[0].plot(range(1000), [expected_random_reward for i in range(1000)], label = "expected random reward", color = "black")

axs[0].set_xlabel("Time steps", fontsize = 20)
axs[0].set_ylabel("Average reward", fontsize = 20)
axs[0].legend(fontsize = 20, loc = "upper left")

axs[1].set_xlabel("Time steps", fontsize = 20)
axs[1].set_ylabel("Optimal action percentage", fontsize = 20)
axs[1].legend(fontsize = 20, loc = "upper left")
plt.show()
