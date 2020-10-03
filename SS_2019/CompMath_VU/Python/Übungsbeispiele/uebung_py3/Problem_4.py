# Problem 4. 2d numpy arrays

import numpy as np


def arrow_matrix(n):
    A = np.identity(n).T
    A = A[::-1]
    A[0, :] = 1
    A[:, n-1] = 1

    return A


print(arrow_matrix(8))
