# integrates f on [a, b] via mile's rule with equidistant nodes of distance h
def Q_4(h, f, a, b):
    n = (b-a)/h
    n = int(n)
    x = np.linspace(a, b, n+1)

    S_11 = f(a)
    S_12 = np.sum(f(x[1:n]))
    S_13 = f(b)
    S_2  = np.sum(f((x[0:n] + x[1:n+1])/2))
    S_41 = np.sum(f((3*x[0:n] + x[1:n+1])/4))
    S_42 = np.sum(f((x[0:n] + 3*x[1:n+1])/4))

    return h/90 * (7*S_11 + 32*S_41 + 12*S_2 + 14*S_12 + 32*S_42 + 7*S_13)