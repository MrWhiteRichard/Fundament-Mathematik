import sympy as sp

t, s, t_0, y01, y02 = sp.symbols('t, s, t_0, y_0^1, y_0^2')

Y = sp.Matrix([[sp.exp(t**2), sp.Rational(1, 9) * (3 * t - 2) * sp.exp(t**2 - 3 * t)], [sp.exp(t**2), sp.Rational(1, 9) * sp.exp(t**2 - 3 * t) * (3 * t - 7)]])

y0 = sp.Matrix([[y01], [y02]])
print("y_0 =")
sp.pretty_print(y0)

b = sp.Matrix([[t * sp.exp(t**2)], [sp.exp(t**2)]])
b = b.subs(t, s)
print("b(s) = ")
sp.pretty_print(b)

Y = sp.simplify(Y)
print("Y(t) = ")
sp.pretty_print(Y)


Y_inv = sp.simplify(Y**-1)
sp.print_latex(y0)
Y_inv = Y_inv.subs(t, s)
print("Y^{-1}(s) = ")
sp.pretty_print(Y_inv)

A = sp.simplify(Y_inv * b)
print("Y^{-1}(s) b(s) =")
sp.pretty_print(A)

B = sp.simplify(sp.integrate(A, (s, t_0, t)))
print("\int_{t_0}^t Y^{-1}(s) b(s) ds =")
sp.pretty_print(B)

C = sp.simplify(Y * B)
print("Y(t) * \int_{t_0}^t Y^{-1}(s) b(s) ds =")
sp.pretty_print(C)

D = sp.simplify(Y_inv.subs(s, t_0) * y0)
print("Y^{-1}(t_0) y_0 = ")
sp.pretty_print(D)

E = sp.simplify(Y * D)
print("Y(t)Y^{-1}t_0 y_0 = ")
sp.pretty_print(E)

result = sp.simplify(E + C)
print("Y(t)Y^{-1}t_0 y_0 + Y(t) * \int_{t_0}^t Y^{-1}(s) b(s) ds  = ")
sp.pretty_print(result)
sp.print_latex(result)


