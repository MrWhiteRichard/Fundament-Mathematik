import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 2

sigma = 1/2
gamma = 1/4

def f(z, t):
    x, y = z
    return [- x * (x - a) * (x - b) - y, sigma * x - gamma * y]

x = np.linspace(-2, 4, 20)
y = np.linspace(-3, 3, 20)

X, Y = np.meshgrid(x, y)

t = 0

u, v = np.zeros(X.shape), np.zeros(Y.shape)

NI, NJ = X.shape

for i in range(NI):
    for j in range(NJ):
        xi = X[i, j]
        eta = Y[i, j]
        etaprime = f([xi, eta], t)
        u[i, j] = etaprime[0]
        v[i, j] = etaprime[1]

Q = plt.quiver(X, Y, u, v)



plt.show()