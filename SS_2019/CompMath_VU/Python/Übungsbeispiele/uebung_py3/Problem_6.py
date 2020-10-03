# Problem 6. tensor product

import numpy as np


class Tensor:
    def tensor1(self, A, B):
        k = A.shape[0]
        n = A.shape[1]
        m = A.shape[2]
        l = B.shape[2]
        C = np.zeros((k, l), dtype = int)

        if n != B.shape[1] or m != B.shape[0]:
            return None

        for i in range(n):
            for j in range(m):
                C[i][j] = np.sum(A[i, :, :] * B[:, :, j])

        return C

    def tensor2(self, A, B):
        k = A.shape[0]
        n = A.shape[1]
        m = A.shape[2]
        l = B.shape[2]
        C = self.tensor1(A, B)

        if n != B.shape[1] or m != B.shape[0]:
            return None

        return np.prod(C, axis = 1)


C = Tensor()

n = 3
m = 3
l = 3
k = 3

A = np.random.randint(10, size = (k, n, m))
B = np.random.randint(10, size = (m, n, l))

print("A = \n", A, "\n")
print("B = \n", B, "\n")

print("\n", "Tensor Product 1:", "A*B = \n", C.tensor1(A, B), "\n")
print("\n", "Tensor Product 1 (for real):", "A*B = \n", np.tensordot(A, B))
print("\n", "Tensor Product 2:", "A*B = \n", C.tensor2(A, B), "\n")
