import numpy as np


def script(x):
    s = np.sign(x)
    M = np.amax(x)
    m = np.array([M]*len(x))
    b = np.array(abs(x) >= m)

    return x - x*b - s*m*b

x = np.array([k - 4 for k in range(8)])

print(x)
print(script(x))
