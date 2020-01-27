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

n = 5000
A = np.random.rand(n,n)
A = np.dot(A,np.transpose(A))
A += 10*np.diag(abs(np.random.random(n)))
b = np.random.rand(n)
tol = 10**(-8)
x0 = np.random.rand(n)*10

xsolve = np.linalg.solve(A,b)

xcg, res, count = cg(A,b,x0,tol)
x = [i+1 for i in range(len(res))]
q = b-A@xcg
print(np.linalg.norm(q))
y = [0.92**i for i in x]
plt.semilogy(x, res, label = "Residuum")
plt.semilogy(x, y, linestyle = "dotted", label = "0.92^t")
plt.xlabel("Iterationen")
plt.legend()
plt.show()
