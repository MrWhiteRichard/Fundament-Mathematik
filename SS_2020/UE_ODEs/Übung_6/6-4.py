import sympy as sp

t, y_hat, E = sp.symbols('t, \hat{y}, E')
#y_hat = sp.symbols('y_hat', cls=sp.Function)

term = 16 * y_hat**3 + 36 * y_hat**2 + 34 * y_hat + 12

sp.pretty_print(term.subs(y_hat, sp.Rational(-3, 4)))
sp.pretty_print(sp.factor(term))

integrand =  term**-1
sp.pretty_print(integrand)
sp.print_latex(integrand)

F = sp.integrate(integrand, y_hat)
sp.pretty_print(F)
sp.print_latex(F)

term2 = y_hat**2 * (16 - 2 * E * t**2) + y_hat * (12 - 3 * E * t**2) + (9 - 2 * E * t**2)
sp.pretty_print(term2)

sol = sp.solve(term2, y_hat)
sp.pretty_print(sol)
sp.print_latex(sol)

term3 = -7 * E**2 * t**4 + 28 * E * t **2 - 432
sp.pretty_print(term3)
term3 = sp.simplify(term3)
sp.pretty_print(term3)
