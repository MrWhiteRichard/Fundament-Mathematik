# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:54:43 2020

@author: Florian
"""

import numpy as np
import time
import matplotlib.pyplot as plt


def zufallsmatrix(n, nonzeros):
	A = np.concatenate((np.zeros((n,nonzeros)), np.random.rand(n, n-nonzeros)), axis = 1)
	for i in range(n):
		np.random.shuffle(A[i])
	return A + A.T + np.diag(np.random.rand(n)*10)


ax1 = plt.subplot2grid((1,6),(0,0),colspan = 4)
ax2 = plt.subplot2grid((1,6),(0,4))
n = 5000
A_base = zufallsmatrix(n,100)
x = [i for i in range(400,n+1,200)]
y = []
for n in x:
	A = A_base[:n,:n]
	b = np.random.rand(n)
	start = time.process_time()
	z = np.linalg.solve(A,b)
	end = time.process_time()
	y.append(end-start)
ax1.loglog(x,y, label = "Rechenzeit")
ax1.loglog(x, (np.array(x)/1000)**3, label = "O(n^3)", linestyle = "dotted")
ax1.legend()
ax1.set_ylabel("Sekunden")
ax1.set_xlabel("Matrix-Dimension")
ax2.axis("Off")
tab = ax2.table(cellText=[[i] for i in y], rowLabels=x, colLabels=["Zeit"], loc = "right")
plt.show()
