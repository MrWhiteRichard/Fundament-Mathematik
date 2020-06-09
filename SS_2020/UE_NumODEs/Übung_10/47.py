import numpy as np
import matplotlib.pyplot as plt

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

def implicit_midpoint(t,y_0,f,df,tol,max_iter):
    y = np.zeros((len(t),2))
    y[0] = y_0
    for i in range(len(t)-1):
        h = t[i+1] - t[i]
        z = [y[i] + h*f(t[i],y[i])]
        #F_i(y) = y - y[i] - h[i]f((t[i]+t[i+1])/2,(y[i] + y)/2)
        z.append(np.linalg.solve(np.identity(2)-h/2*df((t[i]+t[i+1])/2,(y[i] + z[-1])/2),-(z[-1]-y[i]-h*f((t[i]+t[i+1])/2,(y[i] + z[-1])/2))) + z[-1])
        while True:
            j = 1
            z.append(np.linalg.solve(np.identity(2)-h/2*df((t[i]+t[i+1])/2,(y[i] + z[-1])/2),-(z[-1]-y[i]-h*f((t[i]+t[i+1])/2,(y[i] + z[-1])/2))) + z[-1])
            q = np.linalg.norm(z[-1] - z[-2])/np.linalg.norm(z[-2] - z[-3])
            j += 1
            if q >= 1:
                print("PROBLEM!")
            if q/(1-q)*np.linalg.norm(np.linalg.norm(z[-1] - z[-2])) <= tol or j >= max_iter:
                break
        y[i+1] = z[-1]
    return np.array(y)


def symplectic_euler(t,p0,q0,hp,hq,tol,max_iter):
    p = [p0]
    q = [q0]
    for i in range(len(t)- 1):
        h = t[i+1] - t[i]
        z = [p[i] - h*hq(p[i],q[i])]
        p.append(z[-1])
        q.append(q[i] + h*hp(z[-1],q[i]))
    return p,q



l = 10
g = 9.81
tol = 1e-6
max_iter = 10
y0 = np.array([2,1])

def f(t,y):
    return np.array([y[1], -g/l*np.sin(y[0])])
def df(t,y):
    return np.array([[0, 1],[-g/l*np.cos(y[0]),0]])
def hp(p,q):
    return p
def hq(p,q):
    return g/l*np.sin(q)

T =  np.linspace(0,10,10001)
y1 = RK4(T,y0,f)
y2 = implicit_midpoint(T,y0,f,df,1e-6,10)
y3p, y3q = symplectic_euler(T,2,1,hp,hq,tol,max_iter)
plt.plot(T,np.array(y1)[:,0]**2/2 - g/l*np.cos(np.array(y1)[:,1]), label = "RK4")
plt.plot(T,np.array(y2)[:,0]**2/2 - g/l*np.cos(np.array(y2)[:,1]), label = "Implicit Midpoint")
plt.plot(T,np.array(y3p)**2/2 - g/l*np.cos(np.array(y3q)), label = "Symplectic Euler")
plt.legend()
plt.show()
