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


A_base = zufallsmatrix(5000,100)
x = [i for i in range(400,5001,200)]
y = []
for n in x:
	A = A_base[:n,:n]
	b = np.random.rand(n)
	start = time.process_time()
	z = np.linalg.solve(A,b)
	end = time.process_time()
	y.append(end-start)
plt.loglog(x,y, label = "Solving Time")
plt.loglog(x, (np.array(x)/1000)**3, label = "O(n^3)")
plt.legend()
plt.ylabel("Time in seconds")
plt.xlabel("Matrix size")
plt.show()
