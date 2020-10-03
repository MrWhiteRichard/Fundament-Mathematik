import random
import numpy as np

def neville(t, x, y):
    n = len(x) # = len(y)
    
    p = np.zeros((n, n))
    p[:, 0] = y
    
    for m in range(1, n):
        for j in range(0, n-m):
            p[j, m] += (t - x[j])*p[j+1, m-1] - (t - x[j+m])*p[j, m-1]
            p[j, m] /= x[j+m] - x[j]

    return p[0, n-1]

n = random.randint(1, 8)
x = np.random.rand(n)
x = np.around(x, 2)
y = np.random.rand(n)
y = np.around(y, 2)

print('')
print('x =', x)
print('y =', y)
print('')

longbottom = np.array([neville(t, x, y) for t in x])
longbottom = np.around(longbottom, 2)

print('Neville Test:')
print(longbottom)
print(longbottom == y)