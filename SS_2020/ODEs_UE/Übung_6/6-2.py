import sympy as sp

t, a_1, a_2, a_3, a_4 = sp.symbols('t, a_1:5')

### b)

# A = sp.Matrix([[-4, 2, 4, -4], [-2, -4, 4, 4], [4, -4, 0, 0], [4, 4, 0, 0]])
# sp.pretty_print(A)
# b = sp.Matrix([[0], [0], [1], [0]])
# system = A, b 
# sol = sp.linsolve(system , a_1, a_2, a_3, a_4)
# sp.pretty_print(sol)

# # sp.print_latex(A)
# # sp.print_latex(b)

# y_p = a_1 * t * sp.exp(-2 * t) * sp.cos(t) + a_2 * t * sp.exp(-2 * t) * sp.sin(t) + a_3 * sp.exp(-2 * t) * sp.cos(t) + a_4 * sp.exp(-2 * t) * sp.sin(t)

# #y_p = y_p.subs([(a_1, sp.Rational(1,8)), (a_2, sp.Rational(-1, 8)), (a_3, sp.Rational(1,16)), (a_4, sp.Rational(-1,8))])

# print("y_p(t) = ")
# sp.pretty_print(y_p)
# #sp.print_latex(y_p)

# ddy = sp.diff(y_p, t, t)
# print("y_p^primeprime = ")
# sp.pretty_print(ddy)

# lhs = sp.simplify(ddy + y_p)
# print("lhs = ")
# sp.pretty_print(lhs)
# # sp.print_latex(sp.expand(lhs))


### c)
y = sp.symbols('y', cls=sp.Function)

diffeq = sp.Eq(y(t).diff(t, t) - y(t), t * sp.exp(-t))

sp.pretty_print(diffeq)

solc = sp.expand(sp.dsolve(diffeq, y(t)))
#sp.pretty_print(solc)
#sp.print_latex(solc)

y_pc = a_1 * t * sp.exp(-t) + a_2 * t**2 * sp.exp(-t)
sp.print_latex(y_pc)

yc_primeprime = sp.expand(sp.diff(y_pc, t, t))
sp.print_latex(yc_primeprime)

sp.print_latex(yc_primeprime - y_pc)




