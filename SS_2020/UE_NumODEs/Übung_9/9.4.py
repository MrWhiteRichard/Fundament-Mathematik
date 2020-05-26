import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lu_factor, lu_solve

def g(x):
    return np.exp(-30*(x - 1/2)**2)

def M(n):
    return n**2*(np.tri(n-1,n-1,1) - np.tri(n-1,n-1,-2) -3*np.eye(n-1,n-1))

def adams_moulton(alpha,beta,y0,T,Mh):
    n = len(y0)
    h = T[1] - T[0]
    k = len(alpha)
    y = RK4(T[:k],y0,lambda t,y: Mh@y)
    fy = [Mh@y[i] for i in range(k)]
    L,U = lu_factor(np.eye(n) - h*beta[-1]*Mh)
    for i in range(k,len(T)):
        yl = lu_solve((L,U),-alpha@y[-k:] + h*sum([beta[k-j-2]*fy[-j-1] for j in range(k-1)]))
        if np.linalg.norm(yl) > 100:
            return y
        else:
            y.append(yl)
        fy.append(Mh@y[-1])
    return y


def multi_step_method(alpha,beta,y0,T,Mh):
    h = T[1] - T[0]
    k = len(alpha)
    y = RK4(T[:k],y0,lambda t,y: Mh@y)
    fy = [Mh@y[i] for i in range(k)]
    for i in range(k,len(T)):
        yl = h*sum([beta[k-j-1]*fy[-j-1] for j in range(k)]) - alpha@y[-k:]
        if np.linalg.norm(yl) > 100:
            return y
        else:
            y.append(yl)
        fy.append(Mh@y[-1])
    return y


def RK(a,b,c,t,y0,f):
    y=[y0]
    for j in range(1,len(t)):
        k=[f(t[j-1],y[-1])]
        h=t[j]-t[j-1]
        y.append(y[-1]+h*k[0]*b[0])
        for i in range(len(c)):
            k.append(f(t[j-1]+c[i]*h,y[-2]+h*sum([ai*ki for ai,ki in zip(a[i],k)])))
            y[-1]+=h*b[i+1]*k[-1]
    return y

def RK4(t,y,f):
    a=[[1/2],[0,1/2],[0,0,1]]
    b=[1/6,1/3,1/3,1/6]
    c=[1/2,1/2,1]
    return RK(a,b,c,t,y,f)

#Adams-Bashforth
a = np.array([0,0,0,-1])
b = np.array([-9/24,37/24,-59/24,55/24])

#Adams-Moulton
a2 = np.array([0,0,-1])
b2 = np.array([-1/12,8/12,5/12])
a3 = np.array([0,0,0,-1])
b3 = np.array([1/24,-5/24,19/24,9/24])

# BDF
a4 = np.array([3/25,-16/25,36/25,-48/25])
b4 = np.array([0,0,0,12/25])

fig, ((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9)) = plt.subplots(3,3)
ax = [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9]
for i in range(1,10):
    Mh = M(2**i)
    y0 = [g(i/2**i) for i in range(1,2**i)]
    for j in range(2,10):
        t = np.linspace(0,1,2**j+1)
        # fig.suptitle("Adams Bashforth")
        # y = multi_step_method(a,b,y0,t,Mh)

        # fig.suptitle("Adams-Moulton (k = 2)")
        # y = adams_moulton(a2,b2,y0,t,Mh)
        # m = max([np.linalg.norm(y[i]) for i in range(len(y))])

        # fig.suptitle("Adams-Moulton (k = 3)")
        # y = adams_moulton(a3,b3,y0,t,Mh)
        # m = max([np.linalg.norm(y[i]) for i in range(len(y))])
        
        fig.suptitle("BDF")
        y = adams_moulton(a4,b4,y0,t,Mh)


        m = max([np.linalg.norm(y[i]) for i in range(len(y))])
        if m > 10:
            ax[i-1].semilogy(t[:len(y)],[np.linalg.norm(y[i]) for i in range(len(y))], color = "black")
        else:
            ax[i-1].semilogy(t[:len(y)],[np.linalg.norm(y[i]) for i in range(len(y))], label = "tau = 2^{}".format(-j))
    ax[i-1].legend()
    print("FERTIG")
    ax[i-1].set_title("Ortsschrittweite: 2^{}".format(-i))
plt.show()
