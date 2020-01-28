from c import *
import numpy as np
import time
import matplotlib.pyplot as plt

def zufallsmatrix(z,n):
    A = np.zeros([n,n])
    for i in range(n):
        non_zeros = np.random.rand(z)
        zeros = np.zeros(n-z)
        A[i] = np.concatenate((non_zeros, zeros))
        np.random.shuffle(A[i])
    A = A + A.T + np.diag(np.random.rand(n)*1000)
    return A

n = 10000
z = 60
A = zufallsmatrix(z,n)

x = np.array([i for i in range(9000,n+1,200)])
time_np = []
time_sparse = []

for i in x:
    start = 0
    end = 0
    A_part = A[:i,:i]
    b = np.random.rand(i)*100
    start = time.process_time()
    c=np.dot(A_part,b)
    end =time.process_time()
    diff = end-start
    time_np.append(diff)

    A_sparse = Sparse(False,A_part)
    start = time.process_time()
    c=A_sparse.__matmult__(b)
    end = time.process_time()
    diff=end-start
    time_sparse.append(diff)
    print(i)

plt.loglog(x,(x/10000)**2,'--',label="O(n^2)")
plt.loglog(x,time_np,'-',label="numpy")
plt.loglog(x,time_sparse,':',label = "Sparse")
plt.xlabel("Matrix-Dimension")
plt.ylabel("Sekunden")
plt.legend()
plt.show()

# n = 3000
# x = np.array([i for i in range(100,n+1,50)])
# z = 60
# A = zufallsmatrix(z,n)
# tol = 10**(-8)
# time_cg = []
# time_sparse = []
#
# for i in x:
#     start = 0
#     end = 0
#     A_part = A[:i,:i]
#     b = np.random.rand(i)*100
#     x_0 = np.random.rand(i)*100
#     start = time.process_time()
#     xcg = cg(A_part,b,x_0,tol)
#     end =time.process_time()
#     diff = end-start
#     time_cg.append(diff)
#
#     A_sparse = Sparse(False,A_part)
#     start = time.process_time()
#     xScg = Scg(A_sparse,b,x_0,tol)
#     end = time.process_time()
#     diff=end-start
#     time_sparse.append(diff)
#     print(i)
#
# plt.loglog(x,(x/1000)**2,'--',label="O(n^2)")
# plt.loglog(x,time_cg,'-',label="cg")
# plt.loglog(x,time_sparse,':',label = "cg mit Sparse")
# plt.xlabel("Matrix-Dimension")
# plt.ylabel("Sekunden")
# plt.legend()
# plt.show()