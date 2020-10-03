import numpy as np
from scipy.linalg import block_diag


def matrix_1(n):
    A = np.ones((2, 2))
    B = block_diag(*([A] * n))
    
    return B


def matrix_2(n):
    A = np.ones((3, 2))
    B = block_diag(*([A] * n))
    
    return B


print("\n", " A_1 = ", "\n")
print(matrix_1(4), "\n")
print("\n", " A_2 = ", "\n")
print(matrix_2(4), "\n")