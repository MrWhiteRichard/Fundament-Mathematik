# ---------------------------------------------------------------- #

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# ---------------------------------------------------------------- #

# calculate BDF method coefficients

t = sp.Symbol("t")

L = lambda t, j, k : np.prod([(t - (1 - i)) / (i - j) for i in range(k+1) if i != j])

coeffs = []

for k in range(1, 10+1):

    coeffs.append([])

    for j in range(k+1):

        D = sp.lambdify(t, sp.diff(L(t, j, k), t), "numpy")
        coeffs[-1].append(D(1))

    n = len(coeffs[-1]) - 1

# ---------------------------------------------------------------- #

def stability_domain_levels(l, method):

    """
        This function returns the maximum of root absolute values of each point
        in a mesh of complex numbers
        with respec to to a multi-step-method

        l ........ mesh fineness (real and imaginary axis)
        method ... multi-step-method

        This should indicate, how "stable" these points are.
        They SHOULD be
        -   stable, if   ... (< 1) or (= 1 and root is simple)
        - unstabel, else.
    """

    alpha, beta = np.array(method)

    s = len(l)

    # maximum of root absolute values (i.e. spectral radius)
    #   stable, if (< 1) or (= 1 and root is simple)
    # unstabel, else
    stability = np.zeros((s, s))

    # below tolerance ... == 0
    # above tolerance ... != 0
    tol = 1e-8

    for i in range(s):

        for j in range(s):

            # current complex number
            z = l[j] + l[i] * 1j

            # roots of characteristic polynomial sum
            rho_z = alpha + z * beta
            roots = np.roots(rho_z)

            # maximum absolute of roots
            # if maximum <= 1 then all absolute values of roots are
            spectral_radius = max([abs(root) for root in roots])

            if spectral_radius < 1:
                stability[i, j] = spectral_radius

            if abs(spectral_radius - 1) < tol:

                # spectral_radius = 1
                # we'll assume the root is simple
                stability[i, j] = spectral_radius

                for root in roots:

                    # root might not be simple
                    if abs(abs(root) - 1) < tol:

                        # check if root is simple
                        if np.count_nonzero(abs(roots - root) < tol) > 1:

                            # root is not simple, therefore change to a
                            # stupidly high value ... 2
                            # (this point will definitelly not be in stability domain)
                            stability[i, j] = 2
                            break

            if spectral_radius > 1:
                # add
                # stupidly high value ... 2
                # (this point will definitelly not be in stability domain)
                stability[i, j] = 2

    return stability

# ---------------------------------------------------------------- #

# various multi-step-methods

# BDF
bdf1  = [coeffs[0], [1, 0]]
bdf2  = [coeffs[1], [0, 1, 0]]
bdf5  = [coeffs[4], [0, 0, 0, 0, 1, 0]]
bdf10 = [coeffs[9], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

# Adams-Bashforth
bash1 = [[0, -1, 1],       [-1/2, 3/2, 0]]
bash3 = [[0, 0, 0, -1, 1], [-9/24, 37/24, -59/24, 55/24, 0]]

# Adams-Moulton
moulton1 = [[0, -1, 1],       [0, 1/2, 1/2]]
moulton2 = [[0, 0, -1, 1],    [0, -1/12, 8/12, 5/12]]
moulton3 = [[0, 0, 0, -1, 1], [0, 1/24, -5/24, 19/24, 9/24]]

# ---------------------------------------------------------------- #

# plots

fig, axs = plt.subplots(4, 2, figsize = (15, 15))

methods = [bdf1, bdf2, bdf5, bdf10, bash1, bash3, moulton1, moulton3]
axs     = axs.flatten()
names   = ["BDF1 / Impliziter Euler", "BDF2", "BDF5", "BDF10", "Adams-Bashforth (k = 1)", "Adams-Bashforth (k = 3)", "Adams-Moulton (k = 1)", "Adams-Moulton (k = 3)"]

# mesh
l = np.linspace(-3, 3, 64)

for method, ax, name in zip(methods, axs, names):

    # see function doc-string for explanation
    z = stability_domain_levels(l, method)

    # areas
    levelsf = np.linspace(0, 2, 100+1)
    cp = ax.contourf(l, l, z, levels = levelsf)

    # lines
    levels  = np.array([0, 0.1, 0.5, 1, 2])
    CS = ax.contour(l, l, z, levels = levels, colors = 'k')

    # labels
    ax.set_title(name)
    plt.clabel(CS, inline = 1, fontsize = 10)

    # auxilary display
    fig.colorbar(cp, ax = ax)
    ax.grid(True)

fig.tight_layout()
plt.show()

# ---------------------------------------------------------------- #
