import numpy as np
from scipy.optimize import newton_krylov
import matplotlib.pyplot as plt


t = np.linspace(-3,1,1001)
x1,x2,x3 = [],[],[]
def f(y):
    return y + np.tanh(r*y)
for r in t:
    x1.append(newton_krylov(f,-1))
    x2.append(newton_krylov(f,1))
    x3.append(0)

plt.plot(t,x1)
plt.plot(t,x2)
plt.plot(t,x3)
plt.xlabel("r")
plt.ylabel("y*")
plt.show()
