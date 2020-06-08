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


def implicit_euler(t,y_0,f,df,tol,max_iter):
    y = np.zeros((len(t),2))
    y[0] = y_0
    for i in range(len(t)-1):
        h = t[i+1] - t[i]
        z = [y[i] + h*f(t[i],y[i])]
        z.append(np.linalg.solve(np.identity(2)-h*df(t[i+1],z[-1]),-(z[-1]-y[i]-h*f(t[i+1],z[-1]))) + z[-1])
        while True:
            j = 1
            z.append(np.linalg.solve(np.identity(2)-h*df(t[i+1],z[-1]),-(z[-1]-y[i]-h*f(t[i+1],z[-1]))) + z[-1])
            q = np.linalg.norm(z[-1] - z[-2])/np.linalg.norm(z[-2] - z[-3])
            j += 1
            if q >= 1:
                return "PROBLEM!"
            if q/(1-q)*np.linalg.norm(np.linalg.norm(z[-1] - z[-2])) <= tol or j >= max_iter:
                break
        y[i+1] = z[-1]
    return np.array(y)


def symplectic_euler(t,p0,q0,hp,hq,hpq,tol,max_iter):
    p = [p0]
    q = [q0]
    for i in range(len(t)- 1):
        h = t[i+1] - t[i]
        z = [p[i] - h*hq(p[i],q[i])]
        z.append((z[-1] - p[i] + h*hq(z[-1],q[i])/(1-h*hpq(z[-1],q[i])) + z[-1]))
        j = 1
        while True:
            z.append((z[-1] - p[i] + h*hq(z[-1],q[i])/(1-hpq(z[-1],q[i])) + z[-1]))
            r = np.linalg.norm(z[-1] - z[-2])/np.linalg.norm(z[-2] - z[-3])
            j += 1
            if r >= 1:
                print("PROBLEM!:", r)
            if r/(1-r)*np.linalg.norm(np.linalg.norm(z[-1] - z[-2])) <= tol or j >= max_iter:
                print(z)
                break
        p.append(z[-1])
        q.append(q[i] + h*hp(z[-1],q[i]))
    return p,q


l = 10
g = 9.81
tol = 1e-6
max_iter = 10
y0 = np.array([2,1])

def H(t,y):
    return np.array([1/2*y[0]**2, -g/l*np.cos(y[1])])
def dH(t,y):
    return np.array([[y[0], 0],[0,g/l*np.sin(y[1])]])
def hp(p,q):
    return p
def hq(p,q):
    return g/l*np.sin(q)
def hpq(p,q):
    return 0

T =  np.linspace(0,10,1001)
y1 = RK4(T,y0,H)
y2 = implicit_midpoint(T,y0,H,dH,1e-6,10)
y3p, y3q = symplectic_euler(T,2,1,hp,hq,hpq,tol,max_iter)
print(y3p)
#plt.plot(T,np.array(y1)[:,0], label = "RK4")
#plt.plot(T,np.array(y2)[:,0], label = "implicit_midpoint")
plt.plot(T,np.array(y3p),label = "symplectic_euler")
plt.legend()
plt.show()
