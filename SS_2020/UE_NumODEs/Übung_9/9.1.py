import sympy as sp
import numpy as np
t = sp.Symbol("t")


L = lambda t : np.prod([(t - (1 - i))/(i - j) for i in range(k+1) if i != j])
first_roots = []
coeffs = []
for k in range(1,11):
    coeffs.append([])
    for j in range(k+1):
        D = sp.lambdify(t,sp.diff(L(t),t),"numpy")
        coeffs[-1].append(D(1))
    n = len(coeffs[-1]) - 1
    first_roots.append(np.roots(coeffs[-1]))


for i in range(len(first_roots)):
    print("k = {}".format(i+1))
    print([abs(first_roots[i][j]) for j in range(len(first_roots[i]))])
    for j in range(len(first_roots[i])):
        if i < 6:
            if abs(first_roots[i][j]) > 1 - 1e-6:
                n = len(coeffs[i]) - 1
                p = [n*coeffs[i][k] for k in range(n)]
                print(np.polyval(p, first_roots[i][j]))
    print()
