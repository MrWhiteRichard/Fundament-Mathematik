# Problem 2. 2d numpy arrays

import numpy as np


def chessboard_matrix(n):
    A = np.zeros((n, n))
    A[0::2, 0::2] = 1
    A[1::2, 1::2] = 1

    return A


print(chessboard_matrix(8))
