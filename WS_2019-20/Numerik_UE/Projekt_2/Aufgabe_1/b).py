import numpy as np
from itertools import combinations
import time
import matplotlib.pyplot as plt

def cg(A,b,x0,tol):
    xt = x0
    r0 = b - np.dot(A,xt)
    d = r0
    count = 0
    while(np.linalg.norm(r0) > tol):
        prod = np.dot(np.transpose(r0),r0)
        prod2 = np.dot(A,d)
        alpha = prod/np.dot(np.transpose(d),prod2)
        xt = xt + alpha*d
        r0 = r0 - alpha*prod2
        beta = np.dot(np.transpose(r0),r0)/prod
        d = r0 + beta*d
        count += 1
    print(count)
    return xt

n = 5000
A = np.random.rand(n,n)
A = np.dot(A,np.transpose(A))
A += 10*np.diag(abs(np.random.random(n)))
b = np.random.rand(n)
tol = 10**(-8)
x0 = np.random.rand(n)*10

xsolve = np.linalg.solve(A,b)

xcg = cg(A,b,x0,tol)

q = b-A@xcg
print(np.linalg.norm(q))
