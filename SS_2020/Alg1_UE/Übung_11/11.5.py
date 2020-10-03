from sympy import *
import numpy as np
from math import pi


expr = trigsimp(im(a**7))
newexpr = simplify(expr.subs(cos(t)**2,1-sin(t)**2))
newexpr = newexpr.subs(sin(t),t)

print("Polynom:", newexpr)

g = lambdify(t, newexpr, "numpy")

if abs(g(sin(2*pi/7))) < 1e-8:
    print("sin(2Pi/7) ist Nullstelle des Polynoms")

newnewexpr = pdiv(newexpr,(t))[0]

print("Gekürztes Polynom:", imnewnewexpr)


"""
#kann man für Aufgabe 1 verwenden, um die Wurzelausdrücke zu bekommen
expr = trigsimp(re(a**5))

newexpr = simplify(expr.subs(sin(t)**2,1-cos(t)**2))-1
newexpr = newexpr.subs(cos(t),t)

print("Polynom:", newexpr)

f = lambdify(t, newexpr, "numpy")

if abs(f(cos(2*pi/5))) < 1e-8:
    print("cos(2Pi/5) ist Nullstelle des Polynoms")


poldiv = pdiv(newexpr,(t-1))
if poldiv[1] == 0:
    newnewexpr = poldiv[0]

print("Gekürztes Polynom:", newnewexpr)
    """
