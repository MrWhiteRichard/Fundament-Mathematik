def implicit_euler(t, y_0, f, f_y, tol = 1e-6, counter_max = 1e16):

    """
        This function implements the implicit Euler-Method.

        t ............. time steps
        y_0 ........... initial value at t_0 for solution
        f ............. right hand side
        f_y............ derivative with respect to y of right hand side
        tol ........... tolerance for accuracy of F(x)
        counter_max ... maximum iterations for Newton-Method
    """

    # dimension of range of f
    n = len(y_0)

    # t = t_0, ..., t_N
    N = len(t) - 1

    # distance between time steps
    h = t[1::] - t[:-1:]

    # approximated solution
    y = [y_0]

    for ell in range(N):

        F_ell  = lambda y_new: y_new - (y[-1] + h[ell] * f(t[ell+1], y_new))
        DF_ell = lambda y_new: np.eye(n, n) - h[ell] * f_y(t[ell+1], y_new)

#         guess = y[-1]
        guess = y[-1] + h[ell] * f(t[ell], y[-1])

#         y_new = newton(F_ell, DF_ell, guess, tol, counter_max)
        y_new = fsolve(F_ell, guess, xtol = tol)

#         print("Test ...", y_new == y[-1] + h[ell] * f(t[ell+1], y_new))
        y += [y_new]

    y = np.array(y).transpose()

    return y
