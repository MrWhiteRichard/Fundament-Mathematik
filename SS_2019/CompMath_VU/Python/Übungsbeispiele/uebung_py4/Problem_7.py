import numpy as np

def solveU(U, b):
    n = len(b)
    x = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        tmp = b[i]
        
        for j in range(n-1, i, -1):
            tmp -= U[i, j]*x[j]

        x[i] = tmp/U[i, i]

    return x


n = 8

U = np.random.rand(n, n)
b = np.random.rand(n)
U = np.around(U, 2)
b = np.around(b, 2)

for i in range(n):
    for j in range(i):
        U[i, j] = 0

print("\n")
print("U = ", "\n")
print(U, "\n")
print("b = ", b, "\n")

print("Let U*x = b.", "\n")
x = solveU(U, b)
print("x = ", x, "\n")

print("U@x = ", U@x, "\n")
