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
for i in range(n):
    non_zeros = np.random.rand(z)
    zeros = np.zeros(n-z)
    A[i] = np.concatenate((non_zeros, zeros))
    np.random.shuffle(A[i])
A = A + A.T + np.diag(np.random.rand(n)*100)
end = time.process_time()
D = np.diag(np.diagonal(np.sqrt(A)))
print("Kondition alt: {}".format(np.linalg.cond(A)))
print("Kondition neu: {}".format(np.linalg.cond((np.linalg.inv(D)@A)@(np.linalg.inv(D).T))))

A = Sparse(False, A)

print("Zeit Random:{}".format(end-start))

P = D@D.T

start = time.process_time()
xt = vcg(A,b,x0,P,tol)
end = time.process_time()
print("Zeit: {}".format(end - start))
print(np.linalg.norm(A.__matmult__(xt)-b))
