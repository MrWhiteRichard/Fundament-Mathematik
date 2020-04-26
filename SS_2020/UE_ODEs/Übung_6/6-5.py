import sympy as sp

t, s, a_1, a_2, a_3 = sp.symbols('t, s, a_1:4')

y = sp.symbols('y', cls=sp.Function)

diffeq = sp.Eq(y(t).diff(t, 3) - 3 * y(t).diff(t) + 2 * y(t), 9 * sp.exp(t))

sp.pretty_print(diffeq)

sol = sp.expand(sp.dsolve(diffeq, y(t)))

#sp.print_latex(sol)

Y = sp.Matrix([[sp.exp(t), t * sp.exp(t), sp.exp(-2 * t)], [sp.exp(t), sp.exp(t) + t * sp.exp(t), -2 * sp.exp(-2 * t)], [sp.exp(t), 2 * sp.exp(t) + t*sp.exp(t), 4 * sp.exp(-2 * t)]])

#sp.print_latex(Y)

b = sp.Matrix([[0], [0], [9 * sp.exp(t)]])
#sp.print_latex(b)

Yinv = sp.simplify(Y**-1)
#sp.print_latex(Yinv)

temp = sp.simplify(Yinv * b)
#sp.print_latex(temp)

result = sp.integrate(temp, t)
#sp.print_latex(result)
# sp.pretty_print(result)

# sp.pretty_print(sp.expand(Y * result))
# sp.print_latex(sp.expand(Y * result))

### Ansatz

yp = a_1 * sp.exp(t) + a_2 * t * sp.exp(t) + a_3 * t**2 * sp.exp(t)

#sp.print_latex(yp)

dyp = sp.expand(sp.diff(yp, t))
#sp.pretty_print(dyp)
#sp.print_latex(dyp)

dddyp = sp.expand(sp.diff(yp, t, 3))
#sp.print_latex(dddyp)

lhs = dddyp - 3 * dyp + 2 * yp
sp.pretty_print(lhs)
sp.print_latex(lhs)

