# Problem 7. wedge product.

import numpy as np


def wedge_template(*w):
    if len(w) > len(w[0]):
        return None

    def inner(*v):
        n = len(v)
        A = np.zeros((n, n))

        if len(v) > len(v[0]):
            return None

        for i in range(n):
            for j in range(n):
                A[i, j] = np.dot(w[i], v[j])

        # return A
        return np.linalg.det(A)

    return inner


w_1 = np.array([1, 0, 0])
w_2 = np.array([0, 1, 0])
w_3 = np.array([0, 0, 1])

wedge_product = wedge_template(w_1, w_2, w_3)

v_1 = np.array([1, 0, 0]) * 1
v_2 = np.array([0, 1, 0]) * 2
v_3 = np.array([0, 0, 1]) * 4

print(wedge_product(v_1, v_2, v_3))
