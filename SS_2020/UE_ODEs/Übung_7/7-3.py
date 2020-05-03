import sympy as sp

epsilon, t = sp.symbols('epsilon, t')
y = sp.symbols('y', cls=sp.Function)

diffeq = sp.Eq(y(t).diff(t, 2) + y(t) + epsilon * y(t)**3, 0)

sp.pretty_print(diffeq)

sol = sp.dsolve(diffeq, y(t), ics={y(0): 1, y(t).diff(t).subs(t, 0): 0})

sp.pretty_print(sol)