import sympy as sp
import numpy as np
from fractions import Fraction

fraction_matrix = lambda M: [[str(Fraction(y).limit_denominator(100)) for y in x] for x in M]

tau = sp.Symbol('tau')
zeta = sp.Symbol('zeta')

alpha = lambda k, j: float(np.prod([(m + tau) / (m - (k - j)) for m in range(k+1) if m != k-j]).diff(tau).subs(tau, 0))

alphas = [[alpha(k, j) for j in range(k+1)] for k in range(1, 10+1)]

for row in fraction_matrix(alphas):
    print(row)

Roots = [np.roots(alphas_[::-1]) for alphas_ in alphas]

for k, roots in enumerate(Roots):

    print('k =', k+1)

    for root in roots:
        print(round(abs(root), 9))

    print('')
