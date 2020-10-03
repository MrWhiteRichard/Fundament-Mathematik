import numpy as np
from scipy.linalg import lu_solve, lu_factor, block_diag
from math import sqrt
import matplotlib.pyplot as plt
import sympy as sp

def RK(A,b,c,t,y0,M):
    y=[y0]
    n = len(y0)
    m = len(b)
    M_ = block_diag(M,M)
    A_ = np.zeros((m*n,m*n))
    for i in range(m):
        A_[2*i] = np.array([[A[i][j],0] for j in range(m)]).flatten()
        A_[2*i + 1] = np.array([[0,A[i][j]] for j in range(m)]).flatten()
    for j in range(1,len(t)):
        h=t[j]-t[j-1]
        k = np.linalg.solve(np.eye(n*m) - h*M_@A_, np.array(m*list(M@y[-1])))
        sum = 0
        for i in range(m):
            k_i = k[i*n:(i+1)*n]
            sum += b[i]*k_i
        y.append(y[-1] + h*sum)
    return y

def RK_exp(A,b,c,t,y0,M):
    y=[y0]
    for j in range(1,len(t)):
        k=[]
        h=t[j]-t[j-1]
        s = 0
        for i in range(len(c)):
            k.append(M@(y[-1]+h*sum([ai*ki for ai,ki in zip(A[i],k)])))
            s += h*b[i]*k[-1]
        y.append(y[-1]+s)
    return np.array(y)

#Radau-IIA
A1 = np.array([[5/12,-1/12],[3/4,1/4]])
b1 = [3/4,1/4]
c1 = [1/3,1]

#Gauss
A2 = np.array([[1/4,1/4-sqrt(3)/6],[1/4 +sqrt(3)/6, 1/4]])
b2 = [1/2,1/2]
c2 = [1/2- sqrt(3)/6, 1/2 + sqrt(3)/6]


#RK4
A3=np.array([[1/2],[0,1/2],[0,0,1]])
b3=[1/6,1/3,1/3,1/6]
c3=[1/2,1/2,1]
eps = 0.1
y0 = [1,4]
epsilon_ = sp.Symbol('epsilon')
A_ = sp.Matrix([[1,          1],
                    [2/eps, -1/eps]])
t_ = sp.Symbol('t')

solution = sp.exp(t_*A_) @ sp.Matrix(y0)
solution = sp.lambdify([epsilon_, t_], solution)
t = np.linspace(0,1,11)
steps = 1000

M  = np.array([[1,1],[2/eps,-1/eps]])
y1 = RK(A1,b1,c1,t,y0,M)
y2 = RK(A2,b2,c2,t,y0,M)
y3 = RK_exp(A3,b3,c3,t,y0,M)
y4 = [solution(eps,t[i])[0] for i in range(len(t))]
y5 = [solution(eps,t[i])[1] for i in range(len(t))]
print(y4[0])
fig, (p1,p2) = plt.subplots(1,2)
p1.plot(t,np.array(y1), label = "radau")
p1.plot(t,np.array(y2), label = "gauss")
p1.plot(t,np.array(y3), label = "RK4")
p1.plot(t,np.array(y4), label = "Lösung", marker = "x")
p1.plot(t,np.array(y5), label = "Lösung", marker = "x")
p2.plot(t,np.array(y1)[:,0] - np.array(y4).flatten())
p2.plot(t,np.array(y1)[:,0] - np.array(y4).flatten())
p1.legend()
plt.show()
