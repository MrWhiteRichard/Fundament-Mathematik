import sympy as sp
import numpy as np
t = sp.Symbol("t")


L = lambda t : np.prod([(t - (1 - i))/(i - j) for i in range(k+1) if i != j])
coeff = []
for k in range(1,11):
    coeff.append([])
    for j in range(k+1):
        D = sp.lambdify(t,sp.diff(L(t),t),"numpy")
        coeff[-1].append(D(1))

print(coeff)
