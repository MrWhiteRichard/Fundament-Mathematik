import sympy as sp

t, yhat, c = sp.symbols('t, yhat, C')

y_hat, y_tilde = sp.symbols('\hat{y}, \tilde{y}', cls=sp.Function)

# term = 16 * y_hat**3 + 36 * y_hat**2 + 34 * y_hat + 12

# sp.pretty_print(term.subs(y_hat, sp.Rational(-3, 4)))
# sp.pretty_print(sp.factor(term))

# integrand =  term**-1
# sp.pretty_print(integrand)
# sp.print_latex(integrand)

# F = sp.integrate(integrand, y_hat)
# sp.pretty_print(F)
# sp.print_latex(F)

# term2 = y_hat**2 * (16 - 2 * E * t**2) + y_hat * (12 - 3 * E * t**2) + (9 - 2 * E * t**2)
# sp.pretty_print(term2)

# sol = sp.solve(term2, y_hat)
# sp.pretty_print(sol)
# sp.print_latex(sol)

# term3 = -7 * E**2 * t**4 + 28 * E * t **2 - 432
# sp.pretty_print(term3)
# term3 = sp.simplify(term3)
# sp.pretty_print(term3)

# eq1 = sp.Eq(dy_tilde, (- 3 * y_tilde - 4 * id) / (4 * y_tilde + 3 * id))
# sp.pretty_print(eq1)

# eq2 = sp.Eq(y_hat, (- 3 * y_tilde - 4 * id) / (4 * y_tilde + 3 * id))
# sp.pretty_print(eq2)

haty = (- 3 * y_tilde(t) - 4 * t) / (4 * y_tilde(t) + 3 * t)
sp.pretty_print(haty)
sp.print_latex(haty)

tilde_y = sp.solve(sp.Eq(haty, y_hat(t)), y_tilde(t))[0]
sp.pretty_print(tilde_y)
sp.print_latex(tilde_y)

tilde_y_prime = sp.simplify(sp.diff(tilde_y, t))
sp.pretty_print(tilde_y_prime)
sp.print_latex(tilde_y_prime)

sol = sp.simplify(sp.solve(sp.Eq(tilde_y_prime, y_hat(t)), y_hat(t).diff(t))[0])
sp.pretty_print(sol)
sp.print_latex(sol)

F = sp.integrate(((sol * 7 * t)**-1).subs(y_hat(t), yhat), yhat)
sp.pretty_print(F)
sp.print_latex(F)

sol2 = sp.solve(sp.Eq(F + c, sp.log(t) / 7), yhat)
sp.pretty_print(sol2)
sp.print_latex(sol2)

ytilde = sp.simplify(tilde_y.subs(y_hat(t), sol2[1]))
sp.pretty_print(ytilde)
sp.print_latex(ytilde)

y = sp.simplify(ytilde.subs(t, t - 1) - 1)
sp.pretty_print(y)
sp.print_latex(y)

yprime = sp.simplify(sp.diff(y, t))
sp.pretty_print(yprime)
sp.print_latex(yprime)