# ---------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from fractions import Fraction

# ---------------------------------------------------------------- #

beta = lambda n: n / np.sqrt(4 * n**2 - 1)
b = lambda n: np.array([beta(i) for i in range(1, n)])
T = lambda n: np.diag(b(n), 1) + np.diag(b(n), -1)
L = lambda nodes, i, x: np.prod(
    [(x - nodes[j]) / (nodes[i] - nodes[j]) for j in range(len(nodes)) if nodes[i] != nodes[j]]
)

def weights_nodes(a, b, n):

    nodes, vectors = np.linalg.eig(T(n))
    weights = [quad(lambda x: L(nodes, i, x), a, b)[0] for i in range(n)]
    vectors = np.transpose(vectors)
    weights2 = [2*(v[0]/np.linalg.norm(v))**2 for v in vectors]
    return np.array(list(zip(weights, nodes)))

gaussian_quadrature = lambda a, b, n, f: sum([weight * f(node) for weight, node in weights_nodes(a, b, n)])
print(weights_nodes(-1,1,3))
# ---------------------------------------------------------------- #

def test_1(p_max, n):

    for p in range(p_max+1):

        result_decimal  = gaussian_quadrature(0, 1, n, lambda x: x**p)
        result_fraction = str(Fraction(result_decimal).limit_denominator(1000))

        print(result_decimal)
        print(result_fraction)
        print()

# test_1(30, 10)

# ---------------------------------------------------------------- #

def test_polynomial(p_array, n_max):

    a = -1
    b = 1

    for p in p_array:

        approximates = [gaussian_quadrature(a, b, n, lambda x: x**p) for n in range(n_max)]
        exact = b ** (p+1) / (p+1) - a ** (p+1) / (p+1)
        errors = [abs(approximate - exact) for approximate in approximates]

        plt.plot(range(n_max), errors, label = f'$x^{{{p}}}$')

    plt.legend()
    plt.xlabel('$n$')
    plt.ylabel('$\epsilon(n)$')
    plt.grid(linestyle = ':')

    plt.show()

# test_polynomial([1, 2, 4, 8, 16], 10)

# ---------------------------------------------------------------- #


def test(f, n_max, exact):
    a = -1
    b = 1

    approximates = [gaussian_quadrature(a, b, n, f) for n in range(n_max)]
    errors = [abs(approximate - exact) for approximate in approximates]
    print(errors)
    plt.semilogy(range(n_max), errors)

    plt.xlabel('$n$')
    plt.ylabel('$\epsilon(n)$')
    plt.grid(linestyle = ':')

    plt.show()

f = lambda x: np.exp(x)
exact = np.exp(1) - np.exp(-1)

test(f,10,exact)
