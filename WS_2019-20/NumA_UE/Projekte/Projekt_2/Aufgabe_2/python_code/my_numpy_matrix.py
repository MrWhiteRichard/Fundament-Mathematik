def my_numpy_matrix(n):

    assert n >= 2

    h = 1/n

    a = -2 * np.ones(n-1)
    b = np.ones(n-2)

    A = np.diag(b, -1) + np.diag(a, 0) + np.diag(b, 1)
    A = -A/h**2

    return A
