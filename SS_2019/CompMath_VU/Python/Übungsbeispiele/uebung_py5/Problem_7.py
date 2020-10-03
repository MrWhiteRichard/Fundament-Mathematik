import numpy as np
import matplotlib.pyplot as plt


def F(x, y):
    return np.where(x >= 0, (1 - y, 1 + x), (-1 + y, -1 - x))


x = np.linspace(-1, 1, 16)
y = np.linspace(-2, 1, 16)

x, y = np.meshgrid(x, y)


fig, ax = plt.subplots(figsize = (8, 8))
ax.quiver(x, y, *F(x, y))

plt.show()
