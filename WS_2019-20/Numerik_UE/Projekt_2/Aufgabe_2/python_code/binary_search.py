from timeit import default_timer as timer

def recursion(n, c, tol, eigen_pairs, bound_lower, bound_upper):

    bound_middle = rho = (bound_lower + bound_upper)/2

    print("searching for eigen pair with eigen value near", rho, "...")
    start = timer()
    eigen_pair_middle = vector_iteration_shifted(n, c, rho, tol)[1]
    end = timer()
    bound_middle = eigen_pair_middle[0]
    print("found eigen value", bound_middle, "in", end-start, "seconds", "\n")

    if abs(bound_middle - bound_lower) < 10 or bound_middle <= bound_lower:
        print("bound_lower ~ bound_middle")
        print(bound_lower, "~", bound_middle)
        print("or")
        print("bound_middle <= bound_lower")
        print(bound_middle, "<=", bound_lower)
        print("stopping persuit", "\n")
        return False
    if abs(bound_upper - bound_middle) < 10 or bound_upper <= bound_middle:
        print("bound_middle ~ bound_upper")
        print(bound_middle, "~", bound_upper)
        print("or")
        print("bound_upper <= bound_middle")
        print(bound_upper, "<=", bound_middle)
        print("stopping persuit", "\n")
        return False

    eigen_pairs.update([eigen_pair_middle])
    print("eigen_pair_middle (new one) =", eigen_pair_middle, "\n")

    if len(eigen_pairs) == n-1:
        print("len(eigen_pairs) == n-1")
        print(len(eigen_pairs), "=", n-1)
        print("All eigen pairs found", "\n")
        return True

    print("repeating recursion with:")
    print("bound_lower =", bound_lower)
    print("bound_middle =", bound_middle, "\n")
    recursion(n, c, tol, eigen_pairs, bound_lower, bound_middle)

    if len(eigen_pairs) == n-1:
        print("len(eigen_pairs) == n-1")
        print(len(eigen_pairs), "=", n-1)
        print("All eigen pairs found", "\n")
        return True

    print("repeating recursion with:")
    print("bound_middle =", bound_middle)
    print("bound_upper =", bound_upper, "\n")
    recursion(n, c, tol, eigen_pairs, bound_middle, bound_upper)

    return True

def get_my_eigen_pairs_with_vector_iteration(n, c, tol):

    print("Starting search with n =", n, "...", "\n")

    B_inverse_A = my_general_numpy_matrix(n, c)
    eigen_pairs = {}

    rho = 0

    eigen_pair_upper = vector_iteration_unshifted(B_inverse_A, tol)
    bound_upper = eigen_pair_upper[0]

    eigen_pairs.update([eigen_pair_upper])
    print("eigen_pair_upper =", eigen_pair_upper, "\n")

    if len(eigen_pairs) == n-1:
        print("len(eigen_pairs) == n-1")
        print(len(eigen_pairs), "=", n-1)
        print("All eigen pairs found", "\n")
        return eigen_pairs

    eigen_pair_lower = vector_iteration_shifted(n, c, rho, tol)[1]
    bound_lower = eigen_pair_lower[0]

    eigen_pairs.update([eigen_pair_lower])
    print("eigen_pair_lower =", eigen_pair_lower, "\n")

    if len(eigen_pairs) == n-1:
        print("len(eigen_pairs) == n-1")
        print(len(eigen_pairs), "=", n-1)
        print("All eigen pairs found", "\n")
        return eigen_pairs


    print("bound_lower =", bound_lower)
    print("bound_upper =", bound_upper, "\n")
    recursion(n, c, tol, eigen_pairs, bound_lower, bound_upper)

    return eigen_pairs
