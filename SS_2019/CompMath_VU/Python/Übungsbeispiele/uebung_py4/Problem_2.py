import numpy as np

def matrix_1(n):
    if n%2 == 0:
        return None
    
    A = np.zeros((n, n))
    A[::1, 0] = 1
    A[0, ::1] = 1
    A[::1, n-1] = 1
    A[n-1, ::1] = 1
    
    return A

def matrix_2(n):
    if n%2 == 0:
        return None
    
    A = np.zeros((n, n))
    A[::1, n//2] = 1
    
    return A

def matrix_3(n):
    if n%2 == 0:
        return None
    
    x = np.ones(n)
    y = np.zeros(n)
    
    A = np.array([x] + [y, x]*(n//2))
    A[3::4, 0] = 1
    A[1::4, -1] = 1
    
    return A


print("\n")
print(matrix_1(5))
print("\n")
print(matrix_2(5))
print("\n")
print(matrix_3(11))
