import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin

# ist das von der Rebecca aus der Gruppe kopiert
# damit mal was drin ist..
# man muss auch mal was abschreiben ;)
# freePichler

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

def kstepMethod(a,b,h,f,t0,tN,y0):
    k = a.shape[0]
    t = np.linspace(t0,tN,int((tN-t0)/h))
    N = t.shape[0]
    if k == 1:
        y = [y0]
    else:
        y = RK4(t[:k],y0,f)
    fv = [f(t[j],y[j]) for j in range(k)]#damit ich nur einmal pro durchgang auswerten muss
    for j in range(k,N):
        sumy = 0
        sumf = 0
        for i in range(1,k+1):
            sumy+= a[k-i]*y[j-i]
            sumf+= b[k-i]*fv[k-i]
        y.append(-sumy + h*sumf)
        fv.append(f(t[j],y[j]))
        fv.remove(fv[0])
    return y

#Verschiedene Verfahren
#Expliziter Euler
a1 = np.array([-1])
b1 = np.array([1])

a2 = np.array([0,-1])
b2 = np.array([-1/2,3/2])

a3 = np.array([0,0,-1])
b3 = np.array([5/12,-16/12,23/12])

a4 = np.array([0,0,0,-1])
b4 = np.array([-9/24,37/24,-59/24,55/24])
#Example 5.17
#spoiler es sollte dich nicht wundern wenn das nicht konvergiert (vgl.5.28)
a5 = np.array([-5,4])
b5 = np.array([2,4])



#Vergleichsverfahren
def phi(t,y,h,f,b,c,A):
    m = b.shape[0]
    s = y.shape[0]
    k = np.zeros((s,m))

    for i in range(m):
        sum_A = np.zeros(s)
        for j in range(i):
            sum_A += A[i,j]*k[:,j]
        k[:,i] = f(t + c[i]*h, y + h*sum_A)

    return k@b


def runge_kutta(f, t, y_0, b, c, A):
    n = t.shape[0]
    s = y_0.shape[0] #ueberpruefe wie viele funktionen es gibt
    assert( (b.shape[0] == c.shape[0]) & ((b.shape[0],b.shape[0]) == A.shape))
    y = np.zeros((s,n))
    y[:,0]= y_0

    for j in range(n-1):
        h_j = t[j+1]- t[j]
        y[:,j+1] = y[:,j] + h_j*phi(t[j],y[:,j], h_j, f, b, c, A)

    return y

#Example 2.23
#Explizit Euler
def explEuler(f,t,y0):
    b = np.array([1])
    c = np.array([0])
    A = np.zeros((1,1))
    return runge_kutta(f,t,y0,b,c,A)

#TESTING!!!!!!
h = 0.0001

#Problem 2.6
alpha = 2       #geburtenrate der beute
beta = 0.01    #gefressene beute
gamma = 0.01    #zunahme proportional zu den begegnungen
delta = 1 #sterberate der Jäger

def f1(t, y_t): #bekommt 2-dim. array mit (yb(t),yj(t))
    return np.array([alpha*y_t[0] - beta*y_t[1]*y_t[0], gamma*y_t[1]*y_t[0] - delta*y_t[1]])

y1_0= np.array([300,150])

T1 = 10
t1 = np.linspace(0,T1,int(T1/h))
Y1 = kstepMethod(a1,b1,h,f1,0,T1,y1_0)
Y3 = kstepMethod(a3,b3,h,f1,0,T1,y1_0)
Y_expEuler = explEuler(f1,t1,y1_0)

fig1, (ax1,ax2, ax3) = plt.subplots(1,3, figsize=(13,8))
fig1.suptitle("Problem 2.6",fontsize=17)

ax1.plot(t1,Y1)
ax1.set_title("Solution with 1 step")

ax2.plot(t1,Y3)
ax2.set_title("Solution with 3 steps")

ax3.plot(t1,Y_expEuler.T)
ax3.set_title("Solution with expl Euler")
plt.show()


#Problem 5.21
def f2(t,y):
    return np.array([-0.04*y[0] + 10000*y[1]*y[2],
                     0.04*y[0] - 10000*y[1]*y[2] - 3*10000000*y[1]*y[1],
                     3*10000000*y[1]*y[1]])

y2_0 = np.array([1,0,0])

T2 = 10
t2 = np.linspace(0,T2,int(T2/h))
Y2 = kstepMethod(a2,b2,h,f2,0,T2,y2_0)
Y4 = kstepMethod(a4,b4,h,f2,0,T2,y2_0)
Y_RK4 = RK4(t2,y2_0,f2)

fig2, (ax1,ax2, ax3) = plt.subplots(1,3, figsize=(13,8))
fig2.suptitle("Problem 5.21", fontsize=17)

ax1.plot(t2,Y2)
ax1.set_title("Solution with 2 steps")

ax2.plot(t2,Y4)
ax2.set_title("Solution with 4 steps")

ax3.plot(t2,Y_RK4)
ax3.set_title("Solution with RK4")
plt.show()

#Problem 4.17
def f3(t, y):
    A = np.array([[-2,1],[1,-2]])
    v = np.array([2*sin(t), 2*(cos(t)-sin(t))])
    return A@y + v

y3_0 = np.array([2,3])

T3 = 5
t3 = np.linspace(0,T3,int(T3/h))
Y3 = kstepMethod(a3,b3,h,f3,0,T3,y3_0)
Y5 = kstepMethod(a5,b5,h,f3,0,T3,y3_0)

fig3, (ax1,ax2) = plt.subplots(1,2, figsize=(13,8))
fig3.suptitle("Problem 4.17", fontsize=17)

ax1.plot(t3,Y3)
ax1.set_title("Solution with 3 steps")

ax2.plot(t3,Y5)
ax2.set_title("Solution with Ex. 5.17")

plt.show()
