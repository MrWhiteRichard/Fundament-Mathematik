# ---------------------------------------------------------------- #

import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# ---------------------------------------------------------------- #

tol = 1e-6

@np.vectorize
def u(t, x):

    if abs(t - 1) < 1e-3:
        return 0
    else:
        return x / (t - 1)


# ---------------------------------------------------------------- #

fig = plt.figure(figsize = (16, 9))
ax = fig.gca(projection = '3d')

a = -1
b = 1

epsilon = 0.01
dt = 0.01

delta_1 = 0
assert delta_1 < 1 - epsilon
t, x = np.meshgrid(
    np.arange(delta_1, 1 - epsilon, dt),
    np.arange(a, b, dt)
)
# ax.plot_wireframe(t, x, u(t, x))
ax.plot_surface(t, x, u(t, x))

delta_2 = 2
assert delta_2 > 1 + epsilon
t, x = np.meshgrid(
    np.arange(1 + epsilon, delta_2, dt),
    np.arange(a, b, dt)
)
# ax.plot_wireframe(t, x, u(t, x))
ax.plot_surface(t, x, u(t, x))

ax.set_xlabel('$t$')
ax.set_ylabel('$x$')
ax.set_zlabel('$u(t, x)$')

# ---------------------------------------------------------------- #

def show_360(skip = 1, repeat = 1):

    for _ in range(repeat):

        # from https://matplotlib.org/gallery/mplot3d/rotate_axes3d.html ...
        # rotate the axes and update
        for angle in range(0, 360, skip):
            ax.view_init(30, angle)
            plt.draw()
            plt.pause(.001)

# ---------------------------------------------------------------- #

path_name = r'C:\Users\richa\OneDrive\Dokumente\GitHub\Fundament-Mathematik\WS_2020-21\PDEs_UE\Übung_2'
file_name = '2.3.png'
fig.savefig(path_name + '\\' + file_name)