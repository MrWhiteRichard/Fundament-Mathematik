import numpy as np
import time
from c import *
import matplotlib.pyplot as plt

n = 2000
k = 200
z = 10
b = np.random.rand(n)
x0 = np.random.rand(n)
tol = 10**-10
A = np.zeros((n,n))
start = time.process_time()
for i in range(n):
    non_zeros = np.random.rand(z)
    zeros = np.zeros(n-z)
    A[i] = np.concatenate((non_zeros, zeros))
    np.random.shuffle(A[i])
A = A + A.T + np.diag(np.random.rand(n)*100)
end = time.process_time()
D = np.diag(np.diagonal(np.sqrt(A)))
#print("Kondition alt: {}".format(np.linalg.cond(A)))
#print("Kondition neu: {}".format(np.linalg.cond((np.linalg.inv(D)@A)@(np.linalg.inv(D).T))))

print("Zeit Random:{}".format(end-start))

P = D@D.T
x = [i for i in range(k,n+1,k)]
y1 = []
y2 = []
for i in range(k,n+1,k):
    A_i = A[:i,:i]
    b_i = b[:i]
    x0_i = x0[:i]
    P_i = P[:i,:i]
    A_i = Sparse(False, A_i)
    xt, c = Scg(A_i,b_i,x0_i,tol)
    y1.append(c)
    xt, c = vcg(A_i,b_i,x0_i,P_i,tol)
    y2.append(c)
plt.plot(x,y1, label= "Standard", linestyle = "dotted")
plt.plot(x,y2, label = "Vorkonditioniert")
plt.xlabel("Matrixdimension")
plt.ylabel("Anzahl Iterationen")
plt.legend()
plt.show()
