import numpy as np
import matplotlib.pyplot as plt

from scipy import linalg

# quadrature node
omega = lambda m: np.exp(2 * np.pi * 1j / m)

# quadrature on 0-centered ball with radius R
Q_zero = lambda m, f, R: R / m * sum([
    omega(m) ** nu * f(R * omega(m) ** nu)
    for nu in range(m)
])

# quadrature on z-centered ball with radius R
Q = lambda m, f, R, z: Q_zero(m, lambda x: f(x + z), R)

# the big cheese
def integral_method(A, N, j, m, R, z, tol):

    """
    A ... matrix-function
    N ... number of rows/columns of A(lambda)
    j ... number of expected eigen values in ball B_R(z) ...
    m ... number of quadrature nodes
    R ... ball-radius
    z ... ball-center
    tol ... tolerance for singular value decomposition reduction
    """

    # random matrix
    V_hat = np.random.random((N, j))

    # ------------------------ #
    # step 1: calculate A_0

    # integrand of A_0
    def f_0(lamda):

        LU, piv = linalg.lu_factor(A(lamda))
        return np.array([
            linalg.lu_solve((LU, piv), V_hat[:, i])
            for i in range(j)
        ]).T

    # apply quadrature to integrand for A_0
    A_0 = Q(m, f_0, R, z)

    # ------------------------ #
    # step 2: calculate singular value decomposition with J number of singular values

    # get full i.e. unreduced singular value decomposition
    V_tilde, Sigma, W_tilde = linalg.svd(A_0, full_matrices = False)

    # mask for SVD reduction (kill zero values)
    mask = np.abs(Sigma) > tol

    # apply mask i.e. reduce SVD
    Sigma = np.diag(Sigma[mask])
    V_tilde = V_tilde[:, mask]
    W_tilde = W_tilde[mask, :]

    # ------------------------ #
    # step 3: calculate A_1

    # integrand of A_1
    f_1 = lambda lamda: lamda * f_0(lamda)

    # apply quadrature to integrand for A_1
    A_1 = Q(m, f_1, R, z)

    # ------------------------ #
    # step 4: calculate eigen values (e.g. via QR-method)

    return linalg.eigvals(V_tilde.conj().T @ A_1 @ W_tilde.conj().T @ linalg.inv(Sigma))

def plot_complex(number_matrix, title = None, legend = None):

    fig = plt.figure(figsize = (8, 8))

    for number_array in number_matrix:

        plt.scatter(
            *np.array([
                [number.real, number.imag]
                for number in number_array
            ]).T
        )

    plt.grid(linestyle = ':')
    plt.xlabel('$\Re$')
    plt.ylabel('$\Im$')

    if title != None:
        plt.suptitle(title)

    if legend != None:
        plt.legend(legend)

    fig.show()


def plot_complex(number_matrix, title = None, legend = None):

    fig = plt.figure(figsize = (8, 8))

    for number_array in number_matrix:

        plt.scatter(
            *np.array([
                [number.real, number.imag]
                for number in number_array
            ]).T
        )

    plt.grid(linestyle = ':')
    plt.xlabel('$\Re$')
    plt.ylabel('$\Im$')

    if title != None:
        plt.suptitle(title)

    if legend != None:
        plt.legend(legend)

    fig.show()


# ---------------------------------------------------------------- #

def test_1_matrix(eigen_values):

    # diagonal matrix with eigen values in diagonal
    diagonal_matrix = np.diag(eigen_values)

    # transformation matrix
    T = np.random.random(diagonal_matrix.shape)

    # arbitrary matrix with known eigen values
    A = T @ diagonal_matrix @ linalg.inv(T)

    # function A
    A = lambda lamda: T @ diagonal_matrix @ linalg.inv(T) - lamda * np.eye(N)

    return A

# ---------------------------------------------------------------- #

def test_1_get_error_array(eigen_values_exact, N, j, m_array, R, z, tol):

    # get dummy matrix from given exact eigen values
    A = test_1_matrix(eigen_values_exact)

    error_array = []

    for m in m_array:

        # apply integral method
        eigen_values_approx = integral_method(A, N, j, m, R, z, tol)

        # calculate maximum error of eigen value approximation
        error = max([
            min([
                np.abs(approx - exact)
                for exact in eigen_values_exact
            ])
            for approx in eigen_values_approx
        ])

        # append error to array
        error_array.append(error)

    return error_array

# ---------------------------------------------------------------- #

def test_1_plot_error_array(m_array, error_array, reference_order):

    s = reference_order
    reference_label = 'reference:' + ' ' + r'$\mathcal{O}(m^{{{-' + str(s) + r'}}})$'

    fig = plt.figure(figsize = (15, 10))

    plt.loglog(m_array, error_array,      label = 'approximation error')
    plt.loglog(m_array, 1 / m_array ** s, label = reference_label)

    plt.legend()
    plt.xlabel('$m$')
    plt.grid(linestyle = ':')

    fig.show()

# ---------------------------------------------------------------- #

eigen_values_exact = [1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j, 0, 1, 1j, -1j, -1]

A = test_1_matrix(eigen_values_exact)
N = len(eigen_values_exact)
j = 10
m = 2
R = 1.2
z = 1 + 1j
tol = 1e-6

eigen_values_approx = integral_method(A, N, j, m, R, z, tol)

title = 'Integral Method' + '\n' + f'N = {N}, j = {j}, m = {m}, R = {R}, z = {z}, tol = {tol}'
legend = ('exact', 'approx')

plot_complex([eigen_values_exact, eigen_values_approx], title, legend)

eigen_values_exact = [1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j, 0, 1, 1j, -1j, -1]

N = len(eigen_values_exact)
j = 4
m_array = np.array([2, 3, 4, 5, 10, 20, 50, 100, 1000])
R = 1.5
z = 1 + 1j
tol = 1e-6

error_array = test_1_get_error_array(eigen_values_exact, N, j, m_array, R, z, tol)

reference_order = 4
test_1_plot_error_array(m_array, error_array, reference_order)

def test_2_matrix(n, b_0):

    b_1 = lambda j, k: (n + 1 - max(j, k)) * j * k
    b_2 = lambda j, k: n * int(j == k) + 1 / (j + k)

    B_0 = b_0 * np.eye(n)
    B_1 = np.array([[b_1(j+1, k+1) for k in range(n)] for j in range(n)])
    B_2 = np.array([[b_2(j+1, k+1) for k in range(n)] for j in range(n)])

    T = lambda z: (np.exp(z) - 1) * B_1 + z ** 2 * B_2 - B_0

    return T

n = 200
b_0 = 100

T = test_2_matrix(n, b_0)
N = 200
j = 15
m = 50
R = 11.5
z = -30
tol = 1e-6

eigen_values_approx = integral_method(T, N, j, m, R, z, tol)

title = 'Integral Method' + '\n' + f'N = {N}, j = {j}, m = {m}, R = {R}, z = {z}, tol = {tol}'
legend = ('exact', 'approx')

plot_complex([eigen_values_exact, eigen_values_approx], title, legend)
