import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

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

def implicit_euler_fsolve(t,y_0,f,df,tol,max_iter):
    y = np.zeros((len(t),2))
    y[0] = y_0
    for i in range(len(t)-1):
        h = t[i+1] - t[i]
        y[i+1] = fsolve(lambda z: z - y[i] - h*(np.array([[-2,1],[1,-2]])@z + np.array([2*np.sin(t[i+1]),2*(np.cos(t[i+1])-np.sin(t[i+1]))])), y[i] + h*f(t[i],y[i]))
    return np.array(y)

def solve_runge_kutta(f, y_0, t_0, T, A, b1, b2, c, p, h, h_min, tau, l, rho):
    t = [t_0]
    y = [y_0]
    h_array = [0]
    while t[-1] != T:
        h = min(T-t[-1],max(h_min,h))
        k = np.zeros((len(b1),2))
        for j in range(len(b1)):
            k[j] = f(t[-1] + c[j]*h,y[-1] + h*(A[j][:j]@k[:j]))
        F1 = b1@k
        F2 = b2@k
        H = rho*(tau/(np.linalg.norm(F1 - F2)))**(1/p)*h
        if h <= H or h <= h_min:
            t.append(t[-1] + h)
            h_array.append(h)
            y.append(y[-1] + h*F2)
            if t[-1] < T:
                h = min(H,l*h)
        else:
            h = min(H,h/l)
    return t, h_array, np.array(y)

def f_1(t,y):
    return np.array([[-2,1],[1,-2]])@y + np.array([2*np.sin(t),2*(np.cos(t)-np.sin(t))])

def df_1(t,y):
    return np.array([[-2,1],[1,-2]])
y_0 = np.array([2,3])

def f_2(t,z):
    return np.array([[-2,1],[998,-999]])@z + np.array([2*np.sin(t),999*(np.cos(t)-np.sin(t))])

def df_2(t,y):
    return np.array([[-2,1],[998,-999]])

f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex = True)

t = np.linspace(0,10,1001)
y_1 = implicit_euler(t,y_0,f_1,df_1,10**-8,10)
ax1.plot(t,y_1[:,0],"--", label = "Y_1")
ax1.plot(t,y_1[:,1],"--", label = "Y_2")
ax1.set_title("Impliziter Euler")
initital_stepsize = 10**(-5)
min_stepsize = 10**(-10)
tolerance = 10**(-6)
l = 1.5
rho = 0.7

A = np.array([[0,0,0,0,0,0,0],[1/5,0,0,0,0,0,0],[3/40,9/40,0,0,0,0,0],[44/45,-56/15,32/9,0,0,0,0],[19372/6561,-25360/2187,64448/6561,-212/729,0,0,0],
[9017/3168,-355/33,46732/5247,49/176,-5103/18656,0,0],[35/384,0,500/1113,125/192,-2187/6784,11/84,0]])
b1 = np.array([35/384,0,500/1113,125/192,-2187/6784,11/84,0])
b2 = np.array([5179/57600,0,7571/16695,393/640,-92097/339200,187/2100,1/40])
c = np.array([0,1/5,3/10,4/5,8/9,1,1])

t, h, y_2 = solve_runge_kutta(f_1, y_0, 0, 10, A, b1, b2, c, 4, initital_stepsize, min_stepsize, tolerance, l, rho)
ax2.plot(t, y_2[:,0], label = "Y_1")
ax2.plot(t, y_2[:,1], label = "Y_2")
ax2.set_title("Runge-Kutta")
ax3.set_title("Schrittweite (Anzahl Schritte: {0})".format(len(t)))
ax3.plot(t,h)
ax1.legend()
ax2.legend()
ax3.legend()
f2, (ax4, ax5, ax6) = plt.subplots(3, 1, sharex = True)

z_0 = np.array([2,3])
t = np.linspace(0,10,1001)
z_1 = implicit_euler(t,z_0,f_2,df_2,10**-8,10)
ax4.plot(t,z_1[:,0],"--", label = "Z_1")
ax4.plot(t,z_1[:,1],"--", label = "Z_2")
ax4.set_title("Impliziter Euler")

t, h, z_2 = solve_runge_kutta(f_2, y_0, 0, 10, A, b1, b2, c, 4, initital_stepsize, min_stepsize, tolerance, l, rho)
ax5.plot(t, z_2[:,0], label = "Z_1")
ax5.plot(t, z_2[:,1], label = "Z_2")
ax5.set_title("Runge-Kutta")
ax6.set_title("Schrittweite (Anzahl Schritte: {0})".format(len(t)))
ax6.plot(t,h)
ax4.legend()
ax5.legend()
ax6.legend()

plt.show()
