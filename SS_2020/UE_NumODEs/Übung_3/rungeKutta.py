'''collection of explicit runge kutta methods'''

from numpy import array

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

def Heun(t,y,f):
    a=[[1]]
    b=[1/2,1/2]
    c=[1]
    return RK(a,b,c,t,y,f)

def modEuler(t,y,f):
    a=[[1/2]]
    b=[0,1]
    c=[1/2]
    return RK(a,b,c,t,y,f)

def expEuler(t,y,f):
    a=[[]]
    b=[1]
    c=[]
    return RK(a,b,c,t,y,f)
