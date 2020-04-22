import sympy as sp

t = sp.symbols('t')

A1 = sp.Matrix([[-1, 1, -1], [2, -1, 2], [2, 2, -1]])
V1, D1 = A1.diagonalize()
print(A1 ,"=", V1 , D1,  V1**-1)
F1 = sp.exp(t * D1)
print(V1 * F1 * V1**-1)
