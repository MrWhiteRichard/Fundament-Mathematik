# ---------------------------------------------------------------- #

import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# ---------------------------------------------------------------- #

tol = 1e-6

def get_u(eta, zeta):

    @np.vectorize
    def u(r, phi):

        if r == 0:
            r = 2 * np.pi

        if abs(phi) < tol or abs(phi - np.pi) < tol:
            return 0

        elif 0 < phi < np.pi:
            return  eta * np.log(r) + 1

        elif np.pi < phi <= 2 * np.pi:
            return zeta * np.log(r) - 1

        else:
            print(f'ERROR for r = {r}, phi = {phi}')
    
    return u

R = 1

eta = 100
zeta = 100

# ---------------------------------------------------------------- #

fig = plt.figure(figsize = (16, 9))
ax = fig.gca(projection = '3d')

dt = 0.02
r, phi = np.meshgrid(
    np.arange(0, R, dt),
    np.arange(0, 2*np.pi, dt)
)

u = get_u(eta, zeta)

X = r * np.cos(phi)
Y = r * np.sin(phi)
Z = u(r, phi)

# ax.plot_surface(X, Y, Z)
ax.plot_wireframe(X, Y, Z)

# ---------------------------------------------------------------- #

def show_vanilla():
    fig.show()

def save_vanilla():
    fig.savefig('images'+ '/' + f'u, eta = {eta}, zeta = {zeta}.png')

def save_360(elev = 30):

    folder_name = f'u, eta = {eta}, zeta = {zeta}, elev = {elev}'
    os.mkdir('images' + '/' + folder_name)
    for azim in range(0, 360, 10):

        ax.view_init(elev = elev, azim = azim)

        fig_name = f'u, eta = {eta}, zeta = {zeta}, elev = {elev}, azim = {azim}.png'
        fig.savefig('images'+  '/' + folder_name + '/' + fig_name)

def show_360(skip = 1, repeat = 1):

    for _ in range(repeat):

        # from https://matplotlib.org/gallery/mplot3d/rotate_axes3d.html ...
        # rotate the axes and update
        for angle in range(0, 360, skip):
            ax.view_init(30, angle)
            plt.draw()
            plt.pause(.001)

# ---------------------------------------------------------------- #

show_360(4)