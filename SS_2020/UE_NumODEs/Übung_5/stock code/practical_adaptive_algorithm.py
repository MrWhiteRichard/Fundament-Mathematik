def practical_adaptive_algorithm(t_0, T, y_0, f, c, A, b_1, b_2, p, tau, h, h_min, lambda_, rho):

    """
        This function implements the Practical adaptive algorithm
        (from Nannen, Numerics of differential equations, Algorithm 2.35).

        t_0 ... lower bound of interval [t_0, T]
        T ..... upper bound of interval [t_0, T]
        y_0 ... initial value
        f ..... right hand side

        c, A, b_1 ... butcher tableau of           explicit runge-kutta one-step method of order p
        c, A, b_2 ... butcher tableau of auxiliary explicit runge-kutta one-step method of order p+1
        p ........... -

        tau ....... tolerance
        h ......... initial time-step size
        h_min ..... minimal time-step size
        lambda_ ... conformity factor
        rho ....... safety factor
    """

    m = len(c)

    t = [t_0]
    y = [y_0]
    h_array = [0]

    print("initiating practical adaptive algorithm ...", "\n")
    start = timer()

    print("current status ...", round(t[-1]/T * 100, 2), "%")
    print("current time .....", round(timer() - start), "sec")
    print("")
    stop = timer()

    while True:

        # status update each second
        if timer() - stop >= 1:
            print("current status ...", round(t[-1]/T * 100, 2), "%")
            print("passed time ......", round(timer() - start), "sec")
            print("")
            stop = timer()

        h = min(T - t[-1], max(h_min, h))

        k = np.zeros((m, 2))

        for i in range(m):
            k[i] = f(t[-1] + c[i] * h, y[-1] + h * (A[i][:i] @ k[:i]))

        F_1 = b_1 @ k
        F_2 = b_2 @ k

        H  = rho * (tau / (np.linalg.norm(F_1 - F_2)))**(1/p) * h

        if h <= H or h <= h_min:

            t += [t[-1] + h]
            h_array += [h]
            y += [y[-1] + h * F_2]

            if t[-1] < T:
                h = min(H, lambda_ * h)

        else:
            h = min(H, h / lambda_)

        if t[-1] >= T:

            t = np.array(t)
            h = np.array(h_array)
            y = np.array(y).transpose()

            return t, h, y
