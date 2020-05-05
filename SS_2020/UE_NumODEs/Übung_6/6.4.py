import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lu_factor, lu_solve

def g(x):
    return np.exp(-30*(x - 1/2)**2)

def M(n):
    return n**2*(np.tri(n-1,n-1,1) - np.tri(n-1,n-1,-2) -3*np.eye(n-1,n-1))

def U_n(n):
    def f(t,y):
        return M(n)@y
    return f

def explicit_euler(f,t,y0):
    y = [y0]
    for i in range(len(t)-1):
        y.append(y[i] + (t[i+1]-t[i])*f(t[i],y[i]))
    return np.array(y)

def implicit_euler(t,y0,f,n,tol,max_iter):
    y = [np.array(y0)]
    M_n = M(n)
    for i in range(len(t) - 1):
        h = (t[i+1] - t[i])
        y.append(lu_solve(lu_factor(np.eye(n-1) - h*M_n), y[i]))
    return np.array(y)

tol = 10**-6
max_iter = 20
fig, ((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9)) = plt.subplots(3,3)
ax = [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9]
for i in range(1,10):
    f = U_n(2**i)
    y0 = [g(i/2**i) for i in range(1,2**i)]
    for j in range(1,10):
        t = np.linspace(0,1,2**j+1)
        # fig.suptitle("Impliziter Euler")
        # y = implicit_euler(t,y0,f,2**i,tol,max_iter)
        # ax[i-1].semilogy(t,[np.linalg.norm(y[i]) for i in range(len(y))])
        fig.suptitle("Expliziter Euler")
        y = explicit_euler(f,t,y0)
        if j < 2*i+1:
            ax[i-1].semilogy(t,[np.linalg.norm(y[i]) for i in range(len(y))], color = "black")
        else:
            ax[i-1].semilogy(t,[np.linalg.norm(y[i]) for i in range(len(y))], label = "tau = 2^{}".format(-j))
    ax[i-1].legend()
    print("FERTIG")
    ax[i-1].set_title("Ortsschrittweite: 2^{}".format(-i))
plt.show()
