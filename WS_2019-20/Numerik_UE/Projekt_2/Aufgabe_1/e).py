import numpy as np
import time
from c import *


n = 10
z = 2
b = np.random.rand(n)
x0 = np.random.rand(n)
tol = 10**-10
A = np.zeros((n,n))
start = time.process_time()
for i in range(n):
    for j in range(n):
        r1 = np.random.rand(1)
        if r1 < z/n:
            A[i][j] = np.random.rand(1)
A = A + A.T + np.diag(np.random.rand(n)*100)
D = np.diag(np.diagonal(np.sqrt(A)))
print(np.linalg.cond(A))
print(np.linalg.cond((np.linalg.inv(D)@A)@(np.linalg.inv(D).T)))
A = Sparse(False, A)
end = time.process_time()
print(end-start)

P = D@D.T

start = time.process_time()
xt = vcg(A,b,x0,P,tol)
end = time.process_time()
print(end - start)

print(np.linalg.norm(A@xt-b))






