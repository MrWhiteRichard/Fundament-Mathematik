import sympy as sp

epsilon, t, a1, a2 = sp.symbols('epsilon, t, a_1, a_2')
y1 = sp.symbols('y_1', cls=sp.Function)

diffeq = sp.Eq(y1(t).diff(t, 2) + y1(t), -(sp.cos(t))**3)

sp.pretty_print(diffeq)

sol = sp.dsolve(diffeq, y1(t))

sp.pretty_print(sol)

# y1 = 1/(2j - 2*t) * sp.exp(t*1j) + 1/(-2j -2*t) * sp.exp(-t*1j) + sp.Rational(1, 5) * sp.cos(3*t)

# sp.pretty_print(y1)

# sp.pretty_print(sp.simplify(y1.diff(t, 2) + y1))
