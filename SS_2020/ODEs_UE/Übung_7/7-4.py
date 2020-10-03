import numpy as np
import matplotlib.pyplot as plt


# ---------------- #

f = lambda x, y: np.array([y, x**2 + x])

ruhe_x = np.array([0, -1])
ruhe_y = np.array([0,  0])

h = lambda x, y: y**2 - x**2 - 2/3 * x**3

# ---------------- #

border = 0.5

a_x = min(ruhe_x) - border
b_x = max(ruhe_x) + border
n_x = 25

a_y = min(ruhe_y) - border
b_y = max(ruhe_y) + border
n_y = n_x

# ---------------- #

x = np.linspace(a_x, b_x, n_x)
y = np.linspace(a_y, b_y, n_y)

X, Y = np.meshgrid(x, y)
u, v = f(X, Y)
levels = np.linspace(0,1,20)
fig = plt.figure(figsize = (15, 10))
# Option 1: Contourf-Plot

plt.contourf(X, Y, h(X, Y), levels = 20)

# Option 2: Scatter-Plot mit farbigen Kreisen

#plt.scatter(ruhe_x, ruhe_y, marker = 'x', color = 'black', s = 1000)
#plt.scatter(X, Y, c = h(X, Y), s = 250, alpha = 0.25, edgecolors = 'white')

# Ruhelage einzeichnen

plt.scatter(0,0, 200, marker = "x", color = "red")
plt.scatter(-1,0, 200, marker = "x", color = "red")
plt.quiver(X, Y, u, v)
plt.colorbar()

plt.suptitle('Phasenportrait')
plt.grid(linestyle = ':')

plt.show()

# ---------------- #
