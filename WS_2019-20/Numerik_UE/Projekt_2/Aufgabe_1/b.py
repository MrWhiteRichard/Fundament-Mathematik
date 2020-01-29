import numpy as np
from itertools import combinations
import time
import matplotlib.pyplot as plt

def cg(A,b,x0,tol):
    xt = x0
    r0 = b - np.dot(A,xt)
    d = r0
    count = 0
    res = []
    while(np.linalg.norm(r0) > tol):
        prod = np.dot(np.transpose(r0),r0)
        prod2 = np.dot(A,d)
        alpha = prod/np.dot(np.transpose(d),prod2)
        xt = xt + alpha*d
        r0 = r0 - alpha*prod2
        beta = np.dot(np.transpose(r0),r0)/prod
        d = r0 + beta*d
        res.append(np.linalg.norm(r0))
        count += 1
    return xt, np.array(res), count

def zufallsmatrix(n, nonzeros):
	A = np.concatenate((np.zeros((n,nonzeros)), np.random.rand(n, n-nonzeros)), axis = 1)
	for i in range(n):
		np.random.shuffle(A[i])
	return A + A.T + np.diag(np.random.rand(n)*n)

n = 5000
A = zufallsmatrix(n,20)
b = np.random.rand(n)
tol = 10**(-8)
x0 = np.random.rand(n)
cond = np.linalg.cond(A)
c = (1-1/np.sqrt(cond))/(1+1/np.sqrt(cond))
print(cond)
print(c)
xsolve = np.linalg.solve(A,b)

xcg, res, count = cg(A,b,x0,tol)
x = [i+1 for i in range(len(res))]
q = b-A@xcg
print(np.linalg.norm(q))
y1 = [c**i for i in x]
#y2 = [0.9**i for i in x]
plt.semilogy(x, res, label = "Residuum")
plt.semilogy(x, y1, linestyle = "dotted", label = "B^t")
#plt.semilogy(x, y2, linestyle = "dotted", label = "0.9^t")
plt.xlabel("Iterationen")
plt.title("n = {0}, cond(A) = {1}, B = {2}".format(n, cond, c))
plt.legend()
plt.show()
