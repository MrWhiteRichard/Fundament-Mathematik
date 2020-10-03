# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:04:13 2020

@author: Rebecca Weiß

Plot: löse ein explizites Hamilton-system mit verschiedenen methoden
"""

import numpy as np
import matplotlib.pyplot as plt
from rks import RK4, newton
from math import cos,sin

#defining the problem
l = 1
g = 9.81
h = 0.1
T = 10000
y0 = np.array([0,0.1])

def f(t,y):
    return np.array([-g/l*sin(y[1]),y[0]])

def Df(t,y):
    return np.array([[0,-g/l*cos(y[1])],[1,0]])

def H(y):
    return 0.5*y[0]**2 - g/l*cos(y[1])

#methods

def sympl_euler(h,T,y0,f):
    y = [y0]

    for i in range(1,int(T/h)):
        q1 = y[i-1][1] + h*y[i-1][0] #ql+hpl
        p1 = y[i-1][0] - h*g/l*sin(q1) #pl-h*g/l*sin(ql+1)
        y.append(np.array([p1,q1]))
    return y

def midpoint(h,T,y0,f):
    t = np.linspace(0,T,int(T/h))
    y = [y0]

    for i in range(1,int(T/h)):
        y.append(newton(lambda k: k - y[i-1] - h*f(t[i-1]+h/2, y[i-1]/2 + k/2),
                        lambda k : np.eye(len(y0)) - h/2*Df(t[i-1]+h/2,y[i-1]/2 +k/2),
                        f(t[i-1],y[-1]),20,10e-10))
    return y

#TESTING
t = np.linspace(0,T,int(T/h))
Y_RK4 = np.array(RK4(t,y0,f))
Y_mid = np.array(midpoint(h,T,y0,f))
Y_symp = np.array(sympl_euler(h,T,y0,f))
stop = int(10/h)

fig1, p = plt.subplots(3,1, sharex = True, figsize=(13,8))
fig1.suptitle("Mathematisches Pendel: Lösung")

p[0].plot(t[:stop],Y_RK4[:stop])
p[0].set_title("RK4")

p[1].plot(t[:stop],Y_mid[:stop])
p[1].set_title("Midpoint rule")

p[2].plot(t[:stop],Y_symp[:stop])
p[2].set_title("Symplectic Euler")
plt.show()
"""
fig2, p2 = plt.subplots(1,3)
p[0].plot(Y_RK4[0,:],Y_RK4[1,:])
p[1].plot(Y_mid[0,:],Y_mid[1,:])
p[2].plot(Y_symp[0,:],Y_symp[1,:])
plt.show()
"""
fig3, p3 = plt.subplots(3,1,sharex=True, figsize=(13,8))
fig3.suptitle("Erhaltung von H")

p3[0].plot(t,[H(yi) for yi in Y_RK4])
p3[0].set_title("RK4")

p3[1].plot(t,[H(yi) for yi in Y_mid])
p3[1].set_title("Midpoint rule")
#p3[1].set_ylim(-3*1e-9,-8*1e-9)


p3[2].plot(t,[H(yi) for yi in Y_symp])
p3[2].set_title("Symplectic Euler")
#p3[2].set_ylim(-0.0005,-0.0002)


fig4 = plt.figure(figsize=(13,8))
plt.plot(t, [H(yi) for yi in Y_RK4], label = "RK4")
plt.plot(t, [H(yi) for yi in Y_symp],label = "sympl. Euler")
plt.plot(t, [H(yi) for yi in Y_mid], label = "Midpoint", linewidth = 3)
plt.legend()
plt.show()
