# efficient implementation (with loops)

def richardson_extrapolation_2(h_0, f, a, b, r):
    A = np.zeros((r+1, r+1))

    A[0,0] = Q_1(h_0, f, a, b)

    for j in range(r):
        h_j = h_0/2**j
        n_j = int((b-a)/h_j)
        x = np.linspace(a, b, n_j+1)

        A[j+1, 0] = 1/2 * (A[j, 0] + h_j * np.sum(f((x[0:n_j] + x[1:n_j+1])/2)))

    for i in range(1, r+1):
        for j in range(r+1-i):
            A[j, i] = A[j, i-1] + (A[j, i-1] - A[j+1, i-1])/(1/2**(i*2) - 1)

    return A[0, -1]