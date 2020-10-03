# returns i-th lagrange basis polynomial at t via interpolation points x
def L(i, t, x):
    n = len(x) + 1
    dummy = 1

    for j in range(n+1):
        if j != i:
            dummy *= (t - x[j])/(x[i] - x[j])

    return dummy

# calculates closed newton-cotes formula of order n on interval [a, b]
def Q(n):
    a, b = sp.symbols('a b')
    t = sp.Symbol('t')

    h = (b - a)/n
    x = [a + h*i for i in range(n+1)]

    # y_i = f(x_i)
    y = sp.IndexedBase('y')
    y = [y[i] for i in range(n+1)]

    dummy = 0

    for i in range(n+1):
        weight = sp.integrate(L(i, t, x), (t, a, b))
        weight = sp.factor(weight)

        dummy += weight * y[i]

    return sp.factor(dummy)