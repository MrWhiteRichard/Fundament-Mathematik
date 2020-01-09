# integrates f on [a, b] via trapezium rule with equidistant nodes of distance h
def Q_1(h, f, a, b):
    n = (b-a)/h
    n = int(n)
    x = np.linspace(a, b, n+1)

    S_11 = f(a)
    S_12 = np.sum(f(x[1:n]))
    S_13 = f(b)

    return h/2 * (S_11 + 2*S_12 + S_13)