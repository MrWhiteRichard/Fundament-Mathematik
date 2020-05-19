import numpy as np
import matplotlib.pyplot as plt
def multi_step_method(alpha,beta,y0,T,f):
    h = T[1] - T[0]
    k = len(alpha)
    y = RK4(T[:k],y0,f)
    fy = [f(T[i],y[i]) for i in range(k)]
    for i in range(k,len(T)):
        y.append(h*sum([beta[k-j-1]*fy[-j-1] for j in range(k)]) - alpha@y[-k:])
        fy.append(f(T[i],y[-1]))
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
a1 = np.array([-1])
b1 = np.array([1])

a2 = np.array([0,-1])
b2 = np.array([-1/2,3/2])

a3 = np.array([0,0,-1])
b3 = np.array([5/12,-16/12,23/12])

a4 = np.array([0,0,0,-1])
b4 = np.array([-9/24,37/24,-59/24,55/24])

#Example 5.17
a5 = np.array([-5,4])
b5 = np.array([2,4])



#Aufgabe 6
alpha = 2       #geburtenrate der beute
beta = 0.01    #gefressene beute
gamma = 0.01    #zunahme proportional zu den begegnungen
delta = 1 #sterberate der Jäger
y0 = np.array([300,150])

def f1(t, y_t): #bekommt 2-dim. array mit (yb(t),yj(t))
    return np.array([alpha*y_t[0] - beta*y_t[1]*y_t[0], gamma*y_t[1]*y_t[0] - delta*y_t[1]])


T1 = np.linspace(0,10,1001)
Y1 = multi_step_method(a1,b1,y0,T1,f1)
Y3 = multi_step_method(a3,b3,y0,T1,f1)
Y5 = multi_step_method(a5,b5,y0,T1,f1)
Y7 = RK4(T1,y0,f1)

fig1, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2, figsize=(13,8))
fig1.suptitle("Aufgabe 6",fontsize=17)

ax1.plot(T1,Y1)
ax1.set_title("Solution with 1 step")

ax2.plot(T1,Y3)
ax2.set_title("Solution with 3 steps")

ax3.plot(T1,Y5)
ax3.set_title("Solution with Example 5.17")

ax4.plot(T1,Y7)
ax4.set_title("Solution with RK4")
#Aufgabe 21
def f2(t,y):
    return np.array([-0.04*y[0] + 10000*y[1]*y[2],
                     0.04*y[0] - 10000*y[1]*y[2] - 3*10000000*y[1]*y[1],
                     3*10000000*y[1]*y[1]])

y0 = np.array([1,0,0])

T2 = np.linspace(0,1,10001)
Y2 = multi_step_method(a2,b2,y0,T2,f2)
Y4 = multi_step_method(a4,b4,y0,T2,f2)
Y6 = multi_step_method(a5,b5,y0,T2,f2)
Y8 = RK4(T2,y0,f2)
fig2, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2, figsize=(13,8))
fig2.suptitle("Aufgabe 21", fontsize=17)

ax1.plot(T2,Y2)
ax1.set_title("Solution with 2 steps")

ax2.plot(T2,Y4)
ax2.set_title("Solution with 4 steps")

ax3.plot(T2,Y6)
ax3.set_title("Solution with Example 5.17")

ax4.plot(T2,Y8)
ax4.set_title("Solution with RK4")
plt.show()
