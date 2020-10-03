import numpy as np


"""
This function returns a numpy tensor with:
0 on all entries, where indices add up to an even number,
and 1 elsewise.
"""
def tensor(n):
    A = np.zeros((n, n, n))
    A[1::2, 1::2, 1::2] = 1
    A[1::2, 0::2, 0::2] = 1
    A[0::2, 1::2, 0::2] = 1
    A[0::2, 0::2, 1::2] = 1
    
    return A

print(tensor(3))
