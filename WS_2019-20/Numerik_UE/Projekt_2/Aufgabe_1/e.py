import numpy as np
import time
from c import *


n = 1000
z = 10
b = np.random.rand(n)
x0 = np.random.rand(n)
tol = 10**-10
A = np.zeros((n,n))
start = time.process_time()
row_sum = []
for i in range(n):
    non_zeros = np.random.rand(z)
    zeros = np.zeros(n-z)
    A[i] = np.concatenate((non_zeros, zeros))
    np.random.shuffle(A[i])
    #row_sum.append(abs(np.sum(A[i]))+1)
A = A + A.T + np.diag(np.random.rand(n)*10)
end = time.process_time()
D = np.diag(np.diagonal(np.sqrt(A)))
print("Kondition alt: {}".format(np.linalg.cond(A)))
print("Kondition neu: {}".format(np.linalg.cond((np.linalg.inv(D)@A)@(np.linalg.inv(D).T))))

A = Sparse(False, A)

print("Zeit Random:{}".format(end-start))

P = D@D.T
<<<<<<< HEAD
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
plt.title("beliebig s.p.d.")
plt.legend()
plt.show()
=======

start = time.process_time()
xt = vcg(A,b,x0,P,tol)
end = time.process_time()
print("Zeit: {}".format(end - start))
print(np.linalg.norm(A.__matmult__(xt)-b))
>>>>>>> 551652d2362fcc5cd8ee0c76fc77369d0479ff4e
