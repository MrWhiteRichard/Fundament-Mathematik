# ---------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# from scipy.integrate import quad

# ---------------------------------------------------------------- #

beta_scalar = lambda n: n / np.sqrt(4 * n**2 - 1)
beta_vector = lambda n: np.array([beta_scalar(i) for i in range(1, n)])
T = lambda n: np.diag(beta_vector(n), 1) + np.diag(beta_vector(n), -1)
L = lambda nodes, i, x: np.prod(
    [(x - nodes[j]) / (nodes[i] - nodes[j]) for j in range(len(nodes)) if nodes[i] != nodes[j]]
)

def weights_nodes(n):

    eigen_values, eigen_vectors = np.linalg.eig(T(n))
    eigen_vectors = np.transpose(eigen_vectors)

    nodes = eigen_values

    # weights = [quad(lambda x: L(nodes, i, x), a, b)[0] for i in range(n)]
    weights = [(v[0] / np.linalg.norm(v))**2 * 2 for v in eigen_vectors]

    return zip(weights, nodes)

quad_gauss_reference = lambda n, f: sum([weight * f(node) for weight, node in weights_nodes(n)])

Phi = lambda a, b, xi: (a + b + xi * (b - a)) / 2
Phi_inverse = lambda a, b, eta: (2 * eta - (a + b)) / (b - a)
quad_gauss = lambda a, b, n, f: (b - a) / 2 * quad_gauss_reference(n, lambda xi: f(Phi(a, b, xi)))

# ---------------------------------------------------------------- #

# in seconds
PAUSE = 4

def test(a, b, n_max, f, exact, error_theoretical, name):

    n_array = np.array(range(1, n_max))

    approximates = [quad_gauss(a, b, n, f) for n in n_array]
    errors_practical = [abs(exact - approximate) for approximate in approximates]
    errors_theoretical = np.vectorize(error_theoretical)(n_array)

    fig = plt.figure()

    plt.semilogy(n_array, errors_practical,   label = 'practice')
    plt.semilogy(n_array, errors_theoretical, label = 'theory')

    plt.suptitle('Gauß-Quadratur von' + ' ... ' + name)
    plt.xlabel('$n$')
    plt.ylabel('$\epsilon(n)$')
    plt.legend()
    plt.grid(linestyle = ':')

    plt.draw()
    plt.pause(PAUSE)
    # fig.show()

# -------------------------------- #

a = 0
b = 1
n_max = 10

function_data = []

# -------------------------------- #

f = np.exp
F = f
sup = f(b)
name = '$x \mapsto \exp{(x)}$'

function_data.append((f, F, sup, name))

# -------------------------------- #

f = np.sin
F = lambda x : -np.cos(x)
sup = 1
name = '$x \mapsto \sin{(x)}$'

function_data.append((f, F, sup, name))

# -------------------------------- #

f = np.cos
F = np.sin
sup = 1
name = '$x \mapsto \cos{(x)}$'

function_data.append((f, F, sup, name))

# -------------------------------- #

p_array = [1, 2, 4, 8]

for p in p_array:

    f = lambda x: x ** p
    F = lambda x: x ** (p + 1) / (p + 1)
    sup = f(b)
    name = f'$x \mapsto x^{{{p}}}$'

    function_data.append((f, F, sup, name))

# -------------------------------- #

for f, F, sup, name in function_data:

    exact = F(b) - F(a)
    error_theoretical = lambda n: sup * (b - a) ** (2 * n + 3) / np.math.factorial(2 * n + 2)

    test(a, b, n_max, f, exact, error_theoretical, name)

# ---------------------------------------------------------------- #
