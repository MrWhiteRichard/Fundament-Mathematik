import matplotlib.pyplot as plt
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
                resi.append(1)
            else:
                resi.append(0)
        res.append(resi)
    return res


l = np.linspace(-6,6,100) #bei dieser Diskretisierung ist zufällig/ glücklicherweise die Matrix (I-zA) immer invertierbar

# verschiedene Verfahren mit Matrix A und Vektor b
expeuler = [np.array([[0]]),np.array([1])]
impeuler = [np.array([[1]]),np.array([1])]
modeuler = [np.array([[0,0],[1/2,0]]),np.array([0,1])]
imptrapezoidal = [np.array([[0,0],[1/2,1/2]]),np.array([1/2,1/2])]
radau = [np.array([[5/12,-1/12],[3/4,1/4]]),np.array([3/4,1/4])]
gauss = [np.array([[1/4,1/4-np.sqrt(3)/6],[1/4+np.sqrt(3)/6,1/4]]),np.array([1/2,1/2])]


z = stabdomain(l,expeuler)
plt.contourf(l, l ,z)
plt.show()


z = stabdomain(l,impeuler)
plt.contourf(l, l ,z)
plt.show()


z = stabdomain(l,modeuler)
plt.contourf(l, l ,z)
plt.show()


z = stabdomain(l,imptrapezoidal)
plt.contourf(l, l ,z)
plt.show()


z = stabdomain(l,radau)
plt.contourf(l, l ,z)
plt.show()


z = stabdomain(l,gauss)
plt.contourf(l, l ,z)
plt.show()
