# Problem 3. 1d complex numpy arrays

import numpy as np
from measuring_time import tic, toc


def norm_np(x, p):
    return np.sum(abs(x)**p)**(1/p)


def norm(x, p):
    sum = 0

    for y in np.nditer(x):
        sum += abs(y)**p

    return sum**(1/p)


x = np.eye(1, 1_000_000, 0, dtype = complex)
p = 10

print("x = ", x)
print("p = ", p)

tic()
print("Numpy: norm of x:\n", norm_np(x, p))
toc()

tic()
print("Generic: norm of x\n", norm(x, p))
toc()
