# Problem 5. homemade matrix product

import numpy as np
from measuring_time import tic, toc


def matrix_prod_1(A, B):
    m = A.shape[0]
    n = A.shape[1]
    l = B.shape[1]
    C = np.zeros((m, l), dtype = int)

    if n != B.shape[0]:
        return None

    for i in range(m):
        for j in range(l):
                C[i, j] = sum(A[i, :].T * B[:, j])

    return C


def matrix_prod_2(A, B):
    m = A.shape[0]
    n = A.shape[1]
    l = B.shape[1]
    C = np.zeros((m, l), dtype = int)

    if n != B.shape[0]:
        return None

    for i in range(m):
        for j in range(l):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]

    return C

m = 128
n = 128
l = 128

A = np.random.randint(100, size = (m, n))
B = np.random.randint(100, size = (n, l))

print("A = \n", A, "\n")
print("B = \n", B, "\n")

tic()
print("\n", "Matrix Product 1:", "A*B = \n", matrix_prod_1(A, B), "\n")
toc()


tic()
print("\n", "Matrix Product 2:", "A*B = \n", matrix_prod_2(A, B), "\n")
toc()

tic()
print("\n", "A@B = \n", A@B, "\n")
toc()
