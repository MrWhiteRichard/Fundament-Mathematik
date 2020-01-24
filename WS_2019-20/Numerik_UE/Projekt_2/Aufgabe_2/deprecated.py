# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

# calculate determinants of my_numpy_matrix and its variation

def my_determinant_1(n):

    A = my_numpy_matrix(n)

    det = np.linalg.det(A)

    return det

def my_determinant_2(n):

    A = my_numpy_matrix(n)
    A_prime = A/n**2

    det = np.linalg.det(A_prime)

    return det

def calculate_determinants(n_max):

    for n in range(2, n_max):
        det = my_determinant_1(n)
        det = round(det, 4)
        print("det(A_{}) =".format(n), det)

    print("")

    for n in range(2, n_max):
        det = my_determinant_2(n)
        det = round(det, 8)
        print("det(A'_{}) =".format(n), det)

# ---------------------------------------------------------------- #

n_max = 10

#calculate_determinants(n_max)

# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def my_sympy_matrix(n):

    h = 1/n

    def fill(i, j):

        if i == j:
            return -2
        elif i == j-1 or i-1 == j:
            return 1
        else:
            return 0

    A = sp.Matrix(n-1, n-1, fill)

    return A

def calculate_jordan_matrices(n_max):

    print("----------------------------------------------------------------", "\n")

    for n in range(2, n_max+1):
        A = my_sympy_matrix(n)
        print("A_{} =".format(n))
        display(A)

        (P, J) = A.jordan_form()
        print("Jordan normal form of A_{} =".format(n))
        display(J)

        print("----------------------------------------------------------------", "\n")

# ---------------------------------------------------------------- #

n_max = 4

#calculate_jordan_matrices(n_max)

# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #