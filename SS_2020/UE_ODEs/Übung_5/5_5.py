import sympy as sp
sp.init_printing(use_unicode=True)

t, s = sp.symbols('t, s')

Y = sp.Matrix([[sp.exp(t**2), sp.Rational(1, 9) * (3 * t - 2) * sp.exp(t**2 - 3 * t)], [sp.exp(t**2), sp.Rational(1, 9) * sp.exp(t**2 - 3 * t) * (3 * t - 7)]])

print("Y(t) = ")
Y = sp.simplify(Y)
sp.pretty_print(Y)
sp.print_latex(Y)

print("Y^{-1}(t) = ")
Y_inv = sp.simplify(Y**-1)
sp.pretty_print(Y_inv)
sp.print_latex(Y_inv)


