def newton(F, DF, x_0, tol = 1e-6, t_max = 1e16):

    """
        This function implements the Newton-Method
        (from Nannen, Numerik A, Algorithmus 7.12).

        F ....... We search for x such that F(x) = 0.
        DF ...... Jacobian Matrix of F
        x_0 ..... where the iteration starts
        tol ..... tolerance for accuracy of F(x)
        t_max ... maximum iterations for Newton-Method
    """

    x = [x_0]
    Delta_x = [np.linalg.solve(DF(x[0]), -F(x[0]))]
    x += [x[0] + Delta_x[0]]
    t = 0

    while True:

        t += 1
        Delta_x += [np.linalg.solve(DF(x[t]), -F(x[t]))]
        x += [x[t] + Delta_x[t]]

        q_t = np.linalg.norm(Delta_x[t]) / np.linalg.norm(Delta_x[t-1])

        if q_t >= 1:
            print("STOP: Newton-Verfahren konvergiert nicht.")
            return None

        if q_t / (1 - q_t) * np.linalg.norm(Delta_x[t]) <= tol or t > t_max:
            return x[t+1]
