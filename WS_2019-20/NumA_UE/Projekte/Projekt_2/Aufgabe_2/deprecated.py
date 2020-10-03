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

def get_eigen_infos(M, i_max, **kwargs):

    blacklist = []

    if 'blacklist' in kwargs.keys():
        blacklist += kwargs['blacklist']

    data = []

    if not 'matrix' in blacklist:
        data += ["Matrix:"]
        data += [np.array2string(M)]
        data += [""]

    values, vectors = get_sorted_eigen_values_and_vectors(M)
    values  = values [:i_max:]
    vectors = vectors[:i_max:]
    pairs   = zip(values, vectors)

    if not 'eigen_pairs' in blacklist:
        data += ["Eigen-Paare:"]
        data += ["(" + str(value) + "\n" + str(vector) + ")" for value, vector in pairs]
        data += [""]

    if not 'eigen_values' in blacklist:
        data += ["Eigen-Werte:"]
        data += [str(value) for value in values]
        data += [""]

    if not 'eigen_vectors' in blacklist:
        data += ["Eigen-Vektoren:"]
        data += [str(vector) for vector in vectors]
        data += [""]

    return data

# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def show_my_eigen_info(n_min, n_max, i_max, *args, **kwargs):

    assert 2 <= n_min <= n_max

    # will be filled with data ... who could have guessed?
    data = []

    # iterate over matrix sizes
    for n in range(n_min, n_max+1):

        # put header into data
        data += ["n = {}:".format(n)]
        data += ["------" + "-" * int(np.log10(n))]
        data += [""]

        # get matrix
        A = my_numpy_matrix(n)

        # or matrices
        # put data into data
        if 'blacklist' in kwargs.keys():
            data += get_eigen_infos(A, i_max, blacklist = kwargs['blacklist'])
        else:
            data += get_eigen_infos(A, i_max)

    # join data array to data string
    data = "\n".join(data)

    # save me

    file_path = 'data/'
    file_name = 'get_my_eigen_info(n_min = {}, n_max = {}, i_max = {})'.format(n_min, n_max, i_max)

    with open(file_path + file_name + '.txt', 'w') as file:
        file.write(data)

    # show time
    print(data)

# ---------------------------------------------------------------- #

n_min = 2
n_max = n_min + 8
i_max = n_max

blacklist = ['matrix', 'eigen_pairs', 'eigen_vectors']

#show_my_eigen_info(n_min, n_max, i_max, blacklist = blacklist)

# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def show_my_eigen_limits(i_max):

    # will be filled with data ... who could have guessed?
    data = []

    # put data into data
    data += ["n -> inf:"]
    data += ["---------"]
    data += [""]
    data += ["({} * pi)^2 = ".format(j) + str((j * np.pi)**2) for j in range(1, i_max+1)]

    # join data array to data string
    data = "\n".join(data)

    # save me

    file_path = 'data/'
    file_name = 'show_my_eigen_limits(i_max = {})'.format(i_max)

    with open(file_path + file_name + '.txt', 'w') as file:
        file.write(data)

    # show time
    print(data)

# ---------------------------------------------------------------- #

i_max = 4

show_my_eigen_limits(i_max)

# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def plot_eigen_vector(n, i):

    # there are n_max-1 eigen values/vectors at max
    assert i < n

    # get matrix
    A = my_numpy_matrix(n)

    # get sorted eigen vectors
    eigen_vectors = get_sorted_eigen_vectors(A)

    # which eigen vector to plot
    eigen_vector = eigen_vectors[i-1]

    # normalize length
    eigen_vector = eigen_vector/np.amax(abs(eigen_vector))
    # normalize orientation
    eigen_vector = eigen_vector * np.sign(eigen_vector[0])

    n = len(eigen_vector)+1

    # get partition of [0, 1]
    x = np.linspace(0, 1, n+1)
    # get eigen vector with boundary condition
    y = np.concatenate(([0], eigen_vector, [0]))

    # mandatory for adding labels
    fig, ax = plt.subplots()

    # do actual plotting
    plt.plot(x, y, color = 'black')

    # add labels
    ax.set_xlabel("Partitionierung")
    ax.set_ylabel("Eigenvektor mit Randbedingungen")

    # add grid
    plt.grid(linestyle = ':')
 
    # save me
    file_path = 'images/'
    file_name = 'plot_eigen_vector(n = {}, i = {})'.format(n, i)
    plt.savefig(file_path + file_name + '.png')

    # showtime
    plt.show()

# ---------------------------------------------------------------- #

def foo(n_max, i_max):
    for i in range(1, i_max+1):
        for n in range(i+1, n_max+1):
            if m.log(n, 2).is_integer():
                print("i =", i)
                print("n =", n)
                plot_eigen_vector(n, i)

n_max = 128
i_max = 4

#foo(n_max, i_max)

# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def get_my_eigen_info_general(n_min, n_max, i_max, c, **kwargs):

    # there are n_max-1 eigen values/vectors at max
    assert 2 <= n_min <= n_max

    # matrix B would not be regular
    assert c[0] != 0 and c[1] != 0

    # will be filled with data ... who could have guessed?
    data = []

    # iterate over matrix sizes
    for n in range(n_min, n_max+1):

        # put header into data
        data += ["n = {}:".format(n)]
        data += ["------" + "-" * int(np.log10(n))]
        data += [""]

        # get matrix
        B_inverse_A = my_general_numpy_matrix(n, c)

        # put data into data
        if 'blacklist' in kwargs.keys():
            data += get_eigen_infos(B_inverse_A, i_max, blacklist = kwargs['blacklist'])
        else:
            data += get_eigen_infos(B_inverse_A)

    # join data array to data string
    data = "\n".join(data)

    # save me

    file_path = 'data/'
    file_name = 'get_my_eigen_info_general(n_min = {}, n_max = {}, i_max = {}, c = {})'.format(n_min, n_max, i_max, c)

    with open(file_path + file_name + '.txt', 'w') as file:
        file.write(data)

    # show time
    print(data)

# ---------------------------------------------------------------- #

n_min = 1_000
n_max = n_min
i_max = 6
c     = (100, 1)

blacklist = ['matrix', 'eigen_pairs', 'eigen_vectors']

get_my_eigen_info_general(n_min, n_max, i_max, c, blacklist = blacklist)

# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def plot_eigen_vector_general(n, i, c):

    # there are n_max-1 eigen values/vectors at max
    assert i < n

    # matrix B would not be regular
    assert c[0] != 0 and c[1] != 0

    # get matrix
    B_inverse_A = my_general_numpy_matrix(n, c)

    # get sorted eigen vectors
    eigen_vectors = get_sorted_eigen_vectors(B_inverse_A)

    # which eigen vector to plot
    eigen_vector = eigen_vectors[i-1]

    # get plot pair from eigen vector
    x, y = get_plot_pair_from_eigen_vector(eigen_vector)

    # mandatory for adding labels
    fig, ax = plt.subplots()

    # do actual plotting
    plt.plot(x, y, color = 'black')

    # add labels
    ax.set_xlabel("Partitionierung")
    ax.set_ylabel("Eigenvektor mit Randbedingungen")

    # add grid
    plt.grid(linestyle = ':')
 
    # save me
    file_path = 'images/'
    file_name = 'plot_eigen_vector_general(n = {}, i = {}, c = {})'.format(n, i, c)
    plt.savefig(file_path + file_name + '.png')

    # showtime
    plt.show()

# ---------------------------------------------------------------- #

def foo(n_max, i_max, c):
    for i in range(1, i_max+1):
        for n in range(i+1, n_max+1):
            if m.log(n, 2).is_integer():
                print("n =", n)
                print("i =", i)
                print("c =", c)
                plot_eigen_vector_general(n, i, c)

n_max = 128
i_max = 4
c = (6, 1)

#foo(n_max, i_max, c)

# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
