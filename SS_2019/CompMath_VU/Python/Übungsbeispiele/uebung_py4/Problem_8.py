import numpy as np
import math as m

from scipy.linalg import solve
from scipy.integrate import quad

def integrate(x, f, I):
    a = I[0]
    b = I[1]
    n = len(x)
    y = np.array(list(map(f, x)))
    I = np.array([(b**(k+1) - a**(k+1))/(k+1) for k in range(n)])
    X = np.array([x**k for k in range(n)])
    
    Omega = solve(X, I)
    return np.sum(Omega * y)

def f(x): return x**2

n = 8

a = 0
b = 1
I = (a, b)
x = np.array([a + k*(b - a)/n for k in range(n+1)])

print("My integration:", "\n", integrate(x, f, I), "\n")
print("scipy integration & error:", "\n", quad(f, a, b), "\n")

a = 0
b = m.pi/2
I = (a, b)
x = np.array([a + k*(b - a)/n for k in range(n+1)])

f = m.sin
print("My integration:", "\n", integrate(x, f, I), "\n")
print("scipy integration & error:", "\n", quad(f, a, b), "\n")

def f(x): return m.sin(x) + x**2

a = m.pi
b = m.pi * 3.45
I = (a, b)
x = np.array([a + k*(b - a)/n for k in range(n+1)])

print("My integration:", "\n", integrate(x, f, I), "\n")
print("scipy integration & error:", "\n", quad(f, a, b), "\n")