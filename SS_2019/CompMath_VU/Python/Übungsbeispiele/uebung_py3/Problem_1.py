# Problem 1. 2d numpy arrays

import math as m
import numpy as np


def frobeniusnorm_loop(A):
    sum = 0

    for a in np.nditer(A):
        sum += a**2

    return m.sqrt(sum)


def frobeniusnorm(A):
    return m.sqrt(np.sum(A**2))


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("A =\n", A)
print("My frobenius norm:\n", frobeniusnorm(A))
print("Numpy's frobenius norm:\n", np.linalg.norm(A, ord = 'fro'))
