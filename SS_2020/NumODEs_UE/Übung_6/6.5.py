import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def stabdomain(l, method):
    s = len(l)
    res = []
    A = method[0]
    b = method[1]
    m = len(b)

    R = lambda z,M: np.linalg.norm(1 + z*np.dot(np.dot(b,M),np.ones(m)))
    for i in range(s):
        resi = []
        for j in range(s):
            z = l[j] + l[i]*1j
            M = np.linalg.inv(np.eye(m)-z*A) #auf Singularitäten wird hier noch keine Rücksicht genommen - evtl noch verbessern
            if R(z,M) >= 1 :
                resi.append(2)
            else:
                resi.append(R(z,M))
        res.append(resi)
    return res


# verschiedene Verfahren mit Matrix A und Vektor b
expeuler = [np.array([[0]]),np.array([1])]
impeuler = [np.array([[1]]),np.array([1])]
modeuler = [np.array([[0,0],[1/2,0]]),np.array([0,1])]
imptrapezoidal = [np.array([[0,0],[1/2,1/2]]),np.array([1/2,1/2])]
radau = [np.array([[5/12,-1/12],[3/4,1/4]]),np.array([3/4,1/4])]
gauss = [np.array([[1/4,1/4-np.sqrt(3)/6],[1/4+np.sqrt(3)/6,1/4]]),np.array([1/2,1/2])]

fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2)

for method, ax, name in zip([expeuler, impeuler, modeuler, imptrapezoidal, radau, gauss],
[ax1,ax2,ax3,ax4,ax5,ax6], ["Expliziter Euler", "Impliziter Euler", "Modifizierter Euler",
"Implizite Trapezregel", "Radau", "Gauss"]):
    if ax in (ax1,ax3):
        l = np.linspace(-3,3,100)
    else:
        l = np.linspace(-6,6,100)
    levels = levels = np.array([0,0.1,0.5,1,2])
    z = stabdomain(l,method)
    cp = ax.contourf(l,l,z)
    CS = ax.contour(l,l,z, levels=levels, colors='k')
    plt.clabel(CS, inline=1, fontsize=10)
    fig.colorbar(cp, ax = ax)
    ax.set_title(name)
    ax.grid(True)

plt.show()
