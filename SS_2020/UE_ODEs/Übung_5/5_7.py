import sympy as sp

t = sp.symbols('t')
A = sp.Matrix([[2, 1, 0, 0, 0], [0, 2, 0 , 0, 0], [0, -1, 2, 0, 0], [0, 0, 0, 2, 2], [0, 0, 0, -2, 0]])

T, J = A.jordan_form()

sp.pretty_print(A)
sp.pretty_print(J)
sp.pretty_print(T)

K = sp.exp(t * J)

sp.pretty_print(K)

L = (T * K * T**-1).rewrite(sp.sin)

sp.pretty_print(sp.simplify(L))