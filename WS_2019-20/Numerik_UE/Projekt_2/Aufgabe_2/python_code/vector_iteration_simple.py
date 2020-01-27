# m ... number of iterations

def vector_iteration_simple(M, m):

    # some random (non zero) vector
    randy = np.random.rand(M.shape[0])
    # normalize
    randy = randy/np.linalg.norm(randy)

    for _ in range(m):

        # apply matrix
        randy = M @ randy
        # normalize
        randy = randy/np.linalg.norm(randy)

    return randy
