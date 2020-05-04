import numpy as np
import matplotlib.pyplot as plt


def f(z, t):
    x, y = z
    return [y, x**2 + x]

x = np.linspace(-3/2, 1/2, 30)
y = np.linspace(-2, 2, 25)

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