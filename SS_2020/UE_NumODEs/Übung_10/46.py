import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import sympy as sp

t = sp.Symbol("t")


L = lambda t : np.prod([(t - (1 - i))/(i - j) for i in range(k+1) if i != j])
coeffs = []
for k in range(1,11):
    coeffs.append([])
    for j in range(k+1):
        D = sp.lambdify(t,sp.diff(L(t),t),"numpy")
        coeffs[-1].append(D(1))
    n = len(coeffs[-1]) - 1


def stabdomain(l, method):
    alpha = method[0]
    n = len(alpha) - 1
    p = [(n-l)*alpha[l] for l in range(n)]
    beta = method[1]
    s = len(l)
    res = []
    for i in range(s):
        resi = []
        for j in range(s):
            z = l[j] + l[i]*1j
            first_roots = np.roots(alpha + z*np.array(beta))
            x = max([abs(first_roots[j]) for j in range(len(first_roots))] + [0])
            if abs(x-1) < 1e-8:
                resi.append(1)
                for k in range(len(first_roots)):
                    if abs(first_roots[k] - 1) < 1e-8:
                        if abs(np.polyval(p, first_roots[k])) > 1e-8:
                            continue
                        else:
                            resi[-1] = 2
                            break
            else:
                if x < 1:
                    resi.append(x)
                else:
                    resi.append(2)
        res.append(resi)
    return res


# verschiedene Verfahren mit Matrix A und Vektor b
bdf1 = [coeffs[0],[1,0]]
bdf2 = [coeffs[1],[0,1,0]]
bdf5 = [coeffs[4],[0,0,0,0,1,0]]
bdf10 = [coeffs[9],[0,0,0,0,0,0,0,0,0,1,0]]
#Adams-Bashforth
bash1 = [[0,-1,1],[-1/2,3/2,0]]
bash3 = [[0,0,0,-1,1],[-9/24,37/24,-59/24,55/24,0]]

#Adams-Moulton
moulton1 = [[0,-1,1],[0,1/2,1/2]]
moulton2 = [[0,0,-1,1],[0,-1/12,8/12,5/12]]
moulton3 = [[0,0,0,-1,1],[0,1/24,-5/24,19/24,9/24]]


fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6),(ax7,ax8)) = plt.subplots(4,2)

for method, ax, name in zip([bdf1,bdf2,bdf5,bdf10,bash1,bash3,moulton1,moulton3],
[ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8], ["BDF1 / Impliziter Euler", "BDF2", "BDF5", "BDF10",
"Adams-Bashforth (k = 1)", "Adams-Bashforth (k = 3)", "Adams-Moulton (k=1)", "Adams-Moulton (k=3)"]):
    l = np.linspace(-3,3,61)
    levels = np.array([0,0.1,0.5,1,2])
    levelsf = np.linspace(0,2,101)
    z = stabdomain(l,method)
    cp = ax.contourf(l,l,z, levels = levelsf)
    CS = ax.contour(l,l,z, levels=levels, colors='k')
    plt.clabel(CS, inline=1, fontsize=10)
    fig.colorbar(cp, ax = ax)
    ax.set_title(name)
    ax.grid(True)

plt.show()
