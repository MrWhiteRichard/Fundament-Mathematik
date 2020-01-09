# integrates f on [a, b] via simpson's rule with equidistant nodes of distance h
def Q_2(h, f, a, b):
    n = (b-a)/h
    n = int(n)
    x = np.linspace(a, b, n+1)

    S_11 = f(a)
    S_12 = np.sum(f(x[1:n]))
    S_13 = f(b)
    S_2  = np.sum(f((x[0:n] + x[1:n+1])/2))

    return h/6 * (S_11 + 4*S_2 + 2*S_12 + S_13)