from scipy.linalg import lu, solve_triangular

def vector_iteration_shifted(n, c, rho, tol):

    # some random (non zero) vector
    randy = np.random.rand(n-1)
    # normalize
    randy = randy/np.linalg.norm(randy)

    # get matrices
    A = my_numpy_matrix(n)
    B = my_other_numpy_matrix(n, c)
    B_inverse = my_other_numpy_matrix_inverse(n, c)
    B_inverse_A = B_inverse @ A

    # calculate lu-decomposition and apply permutation matrix
    M = A - rho*B
    P, L, U = lu(M)

    # used to get eigen value of randy
    M = np.linalg.inv(A - rho*B) @ B

    # stop iteration when differences are small enough
    eigen_randy_old = -tol
    eigen_randy_new = tol

    while abs(eigen_randy_old - eigen_randy_new) > tol:

        # get eigen values of randy
        eigen_randy_old = np.dot(M @ randy, randy)

        # apply first part of matrix to randy
        randy = P @ B @ randy

        # solve L @ forwards = randy via forwards substitution
        forwards  = solve_triangular(L, randy,    lower = True)
        # solve U @ backwards = forwards per backwards substitution
        backwards = solve_triangular(U, forwards, lower = False)

        # apply second part of matrix to randy
        randy = backwards
        # normalize
        randy = randy/np.linalg.norm(randy)

        # get eigen values of randy
        eigen_randy_new = np.dot(M @ randy, randy)

    # use best approximation of eigen value
    eigen_randy = eigen_randy_new

    # get eigen pair of shifted problem
    eigen_pair_shifted = (eigen_randy, randy)

    # get eigen pair of unshifted problem
    eigen_randy_unshifted = 1/eigen_randy + rho
    eigen_pair_unshifted  = (eigen_randy_unshifted, randy)

    return eigen_pair_shifted, eigen_pair_unshifted
