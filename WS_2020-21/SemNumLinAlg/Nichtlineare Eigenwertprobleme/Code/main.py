import numpy as np
import matplotlib.pyplot as plt

from scipy import linalg
from outsource import *

plt.rc('text', usetex=True)

n = 200
b_0 = 100

b_1 = lambda j, k: (n + 1 - max(j, k)) * j * k
b_2 = lambda j, k: n * int(j == k) + 1 / (j + k)

B_0 = b_0 * np.eye(n)
B_1 = np.array([[b_1(j+1, k+1) for k in range(n)] for j in range(n)])
B_2 = np.array([[b_2(j+1, k+1) for k in range(n)] for j in range(n)])

T = lambda z: (np.exp(z) - 1) * B_1 + z ** 2 * B_2 - B_0

N = n
# ---------------------------------------------------------------- #

j = 20
m = 100
R = 11.5
z = -30
tol = 1e-5

# ---------------------------------------------------------------- #

debug_dict = integral_method(T, N, j, m, R, z, tol, debug = True)
eigen_values_approx = debug_dict['eigen_values']
sigma_full          = debug_dict['Sigma_full']

# integral_method with tol = 0 to avoid masking
eigen_values_fake = integral_method(T, N, j, m, R, z, 0)

# ---------------------------------------------------------------- #

quadrature_nodes = [R * (omega(m) ** nu) + z for nu in range(m)]

# title = 'Approximated eigen values vs. additional values' + '\n' + f'j = {j}, m = {m}, R = {R}, z = {z}, tol = {tol}'
# legend = ('Quadraturpunkte', 'zusätzliche Werte', 'Approximierte Eigenwerte')
#
# plot_complex(
#     [quadrature_nodes, eigen_values_fake, eigen_values_approx],
#     legend = legend,
#     markers_size = 30
# )
#
# ax = plt.figure(figsize = (15, 10)).gca()
#
# singular_value_indices = range(len(sigma_full))
#
# ax.scatter(
#     singular_value_indices,
#     sigma_full
# )
#
# ax.plot(
#     singular_value_indices,
#     [tol] * len(singular_value_indices),
#     color = 'black',
#     label = 'cut-off'
# )
#
# ax.tick_params(axis= "both", labelsize=20)
# ax.set_xlabel('singular value index $n = 1, \dots, j$', fontsize = 20)
# ax.set_ylabel('singular value $\sigma_n$', fontsize = 20)
# ax.set_yscale('log')
# ax.legend(fontsize = 20)
# ax.grid(linestyle = ':')


# ax = plt.figure(figsize = (15, 10)).gca()
#
# eigen_value_indices = range(len(eigen_values_fake))
#
# ax.scatter(
#     eigen_value_indices,
#     [np.linalg.cond(T(ref)) for ref in eigen_values_fake]
# )
#
# ax.plot(
#     eigen_value_indices,
#     [1e15] * len(eigen_value_indices),
#     color = 'black',
#     label = 'cut-off'
# )
#
# ax.tick_params(axis= "both", labelsize=20)
# ax.set_xticks([1,3,5,7,9,11,13,15,17,19])
# ax.set_xlabel('eigen value index $n = 1, \dots, k$', fontsize = 20)
# ax.set_ylabel('condition number cond$(A(\lambda_n))$', fontsize = 20)
# ax.set_yscale('log')
# ax.legend(fontsize = 20)
# ax.grid(linestyle = ':')

# # ---------------------------------------------------------------- #

# we expect only 1 eigen_value,
# take 2 random columns for safety
j = 2

# take 100 quadrature nodes for safety
m = 200

# choose smaller radius to isolate eigen-values
R = 0.5

# the center point will be each eigen value

# choose same tolerance as before
tol = 1e-5

# ---------------------------------------------------------------- #

eigen_values_ref = np.array([
    integral_method(T, N, j, m, R, eigen_value_approx, tol)[0]
    for eigen_value_approx in eigen_values_approx
])

# ---------------------------------------------------------------- #

# ---------------------------------------------------------------- #

# recall initial settings ...
j = 20
z = -30
tol = 1e-5

# some auxilliary parameters
R_offset_array = np.array([0.01, 0.1, 0.5])
R_max = max(abs(z - eigen_values_ref))

# ... and add the rest
m_array = [5, 10, 15, 20, 50, 75, 100]
R_array = R_max - R_offset_array

# ---------------------------------------------------------------- #

error_arrays = [
    [
        max([
            min([
                np.abs(eigen_value_approx - eigen_value_ref)
                for eigen_value_ref in eigen_values_ref
            ])
            for eigen_value_approx in integral_method(T, N, j, m, R, z, tol)
        ])
        for m in m_array
    ]
    for R in R_array
]

# ---------------------------------------------------------------- #

ax = plt.figure(figsize = (15, 10)).gca()

for error_array, R_offset, color in zip(error_arrays, R_offset_array, ['r', 'g', 'b']):
    ax.semilogy(
        m_array,
        error_array,
        color,
        label = '$R_\mathrm{offset} =' + ' ' + str(R_offset) + ' ' + '$'
    )

ax.set_xlabel('number of quadrature nodes $m$')
ax.set_ylabel('$\max$-$\min$-error w.r.t. reference values')

ax.legend()
ax.grid(linestyle = ':')

# ---------------------------------------------------------------- #

# recall initial settings ...
# j = 20
# R = 11.5
# z = -30
# tol = 1e-5
#
# # ... and the rest
# m_array = [10, 20, 30, 40, 50]
# #
# # # ---------------------------------------------------------------- #
# #
# ax = plt.figure(figsize = (15, 10)).gca()
#
# for m in m_array:
#
#     debug_dict = integral_method(T, N, j, m, R, z, tol, debug = True)
#     sigma_full = debug_dict['Sigma_full']
#     singular_value_indices = range(len(sigma_full))
#
#     ax.scatter(
#         singular_value_indices,
#         sigma_full,
#         label = f'$m = {m}$'
#     )
#
# ax.plot(
#     singular_value_indices,
#     [tol] * len(singular_value_indices),
#     color = 'black',
#     label = 'cut-off'
# )
# ax.tick_params(axis= "both", labelsize=20)
# ax.set_xlabel('singular value index $n = 1, \dots, j$', fontsize = 20)
# ax.set_ylabel('singular value $\sigma_n$', fontsize = 20)
# ax.set_yscale('log')
# ax.legend()
# ax.grid(linestyle = ':')
# ---------------------------------------------------------------- #

# ---------------------------------------------------------------- #

# # recall initial settings ...
# m = 200
# R = 11.5
# z = -30
# tol = 1e-5
#
# # ... and the rest
# j_array = [5, 10, 15, 20]
#
# # ---------------------------------------------------------------- #
#
# for j in j_array:
#
#     title = 'Integral Method' + '\n' + f'j = {j}, m = {m}, R = {R}, z = {z}, tol = {tol}'
#     legend = ('quadrature nodes', 'reference eigen values', 'approximate eigen values')
#
#     eigen_values_approx = integral_method(T, N, j, m, R, z, tol)
#
#     plot_complex(
#         [quadrature_nodes, eigen_values_ref, eigen_values_approx],
#         title,
#         legend,
#         markers_size = 30
#     )

# ---------------------------------------------------------------- #

plt.show()
