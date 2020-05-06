import numpy as np
import matplotlib.pyplot as plt

# ---------------- #

a = 2
b = 5

sigma = 1.5
gamma = 1

assert 0 < a < b and sigma > 0 and gamma > 0

f = lambda x, y: np.array([-x * (x - a) * (x - b) - y, sigma * x - gamma * y])

sqrt = np.sqrt( ((a-b) / 2)**2 - sigma/gamma)
ruhe_x = np.array([0, (a+b)/2 - sqrt, (a+b)/2 + sqrt])
ruhe_y = ruhe_x * (sigma/gamma)

# ---------------- #

border = 0.5

a_x = min(ruhe_x) - border
b_x = max(ruhe_x) + border
n_x = 25

a_y = min(ruhe_y) - border - 1.5
b_y = max(ruhe_y) + border + 1.5
n_y = n_x

# ---------------- #

x = np.linspace(a_x, b_x, n_x)
y = np.linspace(a_y, b_y, n_y)

X, Y = np.meshgrid(x, y)
u, v = f(X, Y)

fig = plt.figure(figsize = (15, 10))

plt.quiver(X, Y, u, v)
plt.scatter(ruhe_x, ruhe_y, label = 'Ruhelagen')

title = ''
title += 'Phase Diagram'
title += '\n'
title += '$a = {}$, $b = {}$, $\sigma = {}$, $\gamma = {}$'.format(a, b, sigma, gamma)
plt.suptitle(title)
plt.legend()
plt.grid(linestyle = ':')

plt.show()

# ---------------- #