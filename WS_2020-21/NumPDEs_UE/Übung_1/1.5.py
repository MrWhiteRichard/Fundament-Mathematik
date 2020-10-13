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

def test_1(p_max, n):

    for p in range(p_max+1):

        result_decimal  = quad_gauss(0, 1, n, lambda x: x**p)
        result_fraction = str(Fraction(result_decimal).limit_denominator(1000))

        print(result_decimal)
        print(result_fraction)
        print()

# test_1(30, 10)

# ---------------------------------------------------------------- #

def test_2(p_array, n_max):

    a = 0
    b = 1

    for p in p_array:

        approximates = [quad_gauss(a, b, n, lambda x: x**p) for n in range(n_max)]
        exact = b ** (p+1) / (p+1) - a ** (p+1) / (p+1)
        errors = [abs(approximate - exact) for approximate in approximates]

        plt.plot(range(n_max), errors, label = f'$x^{{{p}}}$')

    plt.legend()
    plt.xlabel('$n$')
    plt.ylabel('$\epsilon(n)$')
    plt.grid(linestyle = ':')

    plt.show()

# test_2([1, 2, 4, 8, 16], 10)

# ---------------------------------------------------------------- #


def test_3(a, b, n_max, f, exact):

    approximates = [quad_gauss(a, b, n, f) for n in range(1, n_max)]
    errors = [abs(exact - approximate) for approximate in approximates]

    plt.plot(range(1, n_max), errors)

    plt.xlabel('$n$')
    plt.ylabel('$\epsilon(n)$')
    plt.grid(linestyle = ':')

    plt.show()

a = -1
b = 1
n_max = 10
f = np.exp
F = f
exact = F(b) - F(a)

test_3(a, b, n_max, f, exact)

# ---------------------------------------------------------------- #
