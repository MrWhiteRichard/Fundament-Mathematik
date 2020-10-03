import numpy as np

def invertL(L):
    n = L.shape[0]
    
    if n == 1:
        return 1/L
    else:
        L_11 = L[0:-1, 0:-1]
        L_12 = np.zeros((n - 1, 1))
        L_21 = L[-1:n, 0:-1]
        L_22 = L[-1:n, -1:n]
        
        return np.block([[invertL(L_11), L_12],
                         [-invertL(L_22)@L_21@invertL(L_11), invertL(L_22)]])

n = 4

L = np.random.rand(n, n)

for i in range(n):
    for j in range(i):
        L[j, i] = 0

print("")
print("L = ", "\n")
print(L, "\n")

"""

L_11 = L[0:-1, 0:-1]
L_12 = np.zeros((n - 1, 1))
L_21 = L[-1:n, 0:-1]
L_22 = L[-1:n, -1:n]

print("L_11 = ", "\n")
print(L_11, "\n")
print("L_21 = ", "\n")
print(L_21, "\n")
print("L_22 = ", "\n")
print(L_22, "\n")

print("L_blocks = ", "\n")
print(np.block([[L_11, L_12],
                [L_21, L_22]]), "\n")

"""

L_inv = invertL(L)
print("L_inv = ", "\n")
print(L_inv, "\n")



E_n = abs(np.around(L @ L_inv, 12))
print("L @ L_inv = ", "\n")
print(E_n, "\n")
