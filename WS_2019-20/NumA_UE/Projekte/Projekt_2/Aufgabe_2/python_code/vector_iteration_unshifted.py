def vector_iteration_unshifted(M, tol):

    # some random (non zero) vector
    randy = np.random.rand(M.shape[0])
    # normalize
    randy = randy/np.linalg.norm(randy)

    # stop iteration when differences are small enough
    eigen_randy_old = -tol
    eigen_randy_new = tol

    while abs(eigen_randy_old - eigen_randy_new) > tol:

        # get eigen values of randy
        eigen_randy_old = np.dot(M @ randy, randy)

        # apply matrix
        randy = M @ randy
        # normalize
        randy = randy/np.linalg.norm(randy)

        # get eigen values of randy
        eigen_randy_new = np.dot(M @ randy, randy)

    # use best approximation of eigen value
    eigen_randy = eigen_randy_new

    # get eigen pair
    eigen_pair = (eigen_randy, randy)

    return eigen_pair
