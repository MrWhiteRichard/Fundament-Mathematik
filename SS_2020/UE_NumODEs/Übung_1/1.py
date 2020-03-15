import numpy as np
import math as m
import matplotlib.pyplot as plt

n = 100
y_real = m.sqrt(np.exp(1))
y_error = []
for j in range(1,n):
    y = [1]
    for i in range(j):
        y.append(y[-1]+i/(j**2)*y[-1])
    y_error.append(np.abs(y[-1]-y_real))

print(y_error)
plt.loglog([j for j in range(1,n)], y_error, label = "Fehler")
plt.loglog([j for j in range(1,n)], [j**-1 for j in range(1,n)], label = "O(1/n)")
plt.xlabel("Anzahl Zerlegungspunkte")
plt.ylabel("absoluter Fehler")
plt.legend()
plt.show()
