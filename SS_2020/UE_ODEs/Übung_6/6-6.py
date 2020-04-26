import sympy as sp

tau, t = sp.symbols('\tau, t')

y = sp.symbols('y', cls=sp.Function)

diffeq = sp.Eq(2 * t**3 * y(t).diff(t,3) + 10 * t**2 * y(t).diff(t,2) - 4 * t * y(t).diff(t) - 20 * y(t), 0)

sp.pretty_print(diffeq)

sol = sp.expand(sp.dsolve(diffeq, y(t)))

sp.pretty_print(sol)
sp.print_latex(sol)

diffeq2 = sp.Eq(2 * sp.exp(tau)**3 * y(tau).diff(tau,3) + 10 * sp.exp(tau)**2 * y(tau).diff(tau,2) - 4 * sp.exp(tau) * y(tau).diff(tau) - 20 * y(tau), 0)

sp.pretty_print(diffeq2)

sol2 = sp.expand(sp.dsolve(diffeq2, y(tau)))

sp.pretty_print(sol2)