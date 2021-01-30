# ---------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt

from scipy import linalg

# ---------------------------------------------------------------- #

# quadrature node
omega = lambda m: np.exp(2 * np.pi * 1j / m)

# quadrature on 0-centered ball with radius R
Q_zero = lambda m, f, R: R / m * sum([
    omega(m) ** nu * f(R * omega(m) ** nu)
    for nu in range(m)
])

# quadrature on z-centered ball with radius R
Q = lambda m, f, R, z: Q_zero(m, lambda x: f(x + z), R)

# ---------------------------------------------------------------- #

def integral_method(A, N, j, m, R, z, tol, debug = False):

    """
    A ... matrix-function
    N ... number of rows/columns of A(lambda)
    j ... number of expected eigen values in ball B_R(z)
    m ... number of quadrature nodes
    R ... ball-radius
    z ... ball-center
    tol ... tolerance for SVD reduction
    """

    # random matrix
    V_hat = np.random.random((N, j))

    # ------------------------ #
    # step 1:
    # calculate A_0 and A_1

    # integrand of A_0 and A_1 (with index 0 resp. 1)
    def integrand(index, lamda):

        LU, piv = linalg.lu_factor(A(lamda))

        return lamda ** index * np.array([
            linalg.lu_solve((LU, piv), V_hat[:, i])
            for i in range(j)
        ]).T

    f_0 = lambda lamda: integrand(0, lamda)
    f_1 = lambda lamda: integrand(1, lamda)

    # apply quadrature formula to integrand for A_0 and A_1
    A_0 = Q(m, f_0, R, z)
    A_1 = Q(m, f_1, R, z)

    # ------------------------ #
    # step 2:
    # calculate SVD
    # reduce to J singular values

    # get full i.e. unreduced SVD
    V_tilde_full, Sigma_full, W_tilde_full = linalg.svd(
        A_0,
        full_matrices = False
    )

    # mask for SVD reduction (kill zero values)
    mask = np.abs(Sigma_full) > tol

    # apply mask i.e. reduce SVD
    Sigma_reduced = Sigma_full[mask]
    V_tilde_reduced = V_tilde_full[:, mask]
    W_tilde_reduced = W_tilde_full[mask, :]

    # ------------------------ #
    # step 3:
    # calculate eigen values of linearized problem

    matrices = (
        V_tilde_reduced.conj().T,
        A_1,
        W_tilde_reduced.conj().T,
        np.diag(Sigma_reduced ** (-1))
    )

    eigen_values = linalg.eigvals(
        matrices[0] @ matrices[1] @ matrices[2] @ matrices[3]
    )

    if debug:
        return {
            'eigen_values': eigen_values,
            'V_hat': V_hat,
            'integrand': integrand, 
            'f_0': f_0, 
            'f_1': f_1,
            'A_0': A_0, 
            'A_1': A_1,
            'V_tilde_full': V_tilde_full, 
            'Sigma_full': Sigma_full, 
            'W_tilde_full': W_tilde_full,
            'V_tilde_reduced': V_tilde_reduced, 
            'Sigma_reduced': Sigma_reduced, 
            'W_tilde_reduced': W_tilde_reduced
        }
    else:
        return eigen_values

# ---------------------------------------------------------------- #

def plot_complex(
    number_matrix,
    title = None, legend = None,
    figure_size = (15, 10),
    markers_size = None, markers_shapes = None
):

    if markers_size == None:
        markers_size = plt.rcParams['lines.markersize'] ** 2

    if markers_shapes == None:
        markers_shapes = ['o'] * len(number_matrix)

    fig = plt.figure(figsize = figure_size)

    for i, number_array in enumerate(number_matrix):

        plt.scatter(
            *np.array([
                [number.real, number.imag]
                for number in number_array
            ]).T,
            s = markers_size,
            marker = markers_shapes[i]
        )

    if title != None:
        plt.suptitle(title)

    if legend != None:
        plt.legend(legend)

    plt.xlabel('$\Re$')
    plt.ylabel('$\Im$')
    plt.grid(linestyle = ':')

    fig.show()

# ---------------------------------------------------------------- #
