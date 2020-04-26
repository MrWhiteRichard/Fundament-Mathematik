'''collection of runge kutta methods'''

from numpy import array,linalg,eye,ones,empty,diag,prod,concatenate,zeros

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

def RK45step(t,y,h,f):
    a=[     [1/5],
            [3/40,9/40],
            [44/45,-56/15,32/9],
            [19372/6561,-25360/2187,64448/6561,-212/729],
            [9017/3168,-355/33,46732/5247,49/176,-5103/18656],
            [35/384,0,500/1113,125/192,-2187/6784,11/84]]
    b5=[35/384,0,500/1113,125/192,-2187/6784,11/84,0]
    b4=[5179/57600,0,7571/16695,393/640,-92097/339200,187/2100,1/40]
    c=[1/5,3/10,4/5,8/9,1,1]
    k=[f(t,y)]
    for j in range(len(c)):
        k.append(f(t+c[j]*h,y+h*sum([ai*ki for ai,ki in zip(a[j],k)])))
    y4=(y+h*sum([bi*ki for bi,ki in zip(b4,k)]))
    y5=(y+h*sum([bi*ki for bi,ki in zip(b5,k)]))
    return y4,y5

def stepandest_rk45(t0,y0,h,f):
    y4,y5=RK45step(t0,y0,h,f)
    return y5,linalg.norm(y4-y5)

def adaptive(t0,y0,tmax,f,hmin,tol,rho,eta,stepandest,order):
    """general adaptive method, stepandest has input (t0,y0,h,f) \
    and output (y,est)"""
    t=[t0]
    y=[y0]
    #h=tmax-t0
    h=hmin
    numrefs=0
    #h=0.1*tol**(1/order)
    while t[-1]<tmax:
        yapp,est=stepandest(t[-1],y[-1],h,f)
        if (est<=tol*h or h<=hmin):
            h=max(h,hmin)
            #print('error estimate={}'.format(est))
            #print('step accepted with h={}'.format(h))
            y.append(yapp)
            t.append(t[-1]+h)
            tmp=h*eta
            if est>0:
                tmp=rho*(tol/est*h**(order+1))**(1/order)
            h=min(max(hmin, min(h*eta,tmp)),tmax-t[-1])
        else:
            #print('refining')
            numrefs+=1
            h=max(hmin,h/2)
    return y,t,numrefs

def newton(f,fprime,x0,maxit,tol):
    x=x0
    its=0
    while its<maxit and linalg.norm(f(x))>tol:
        x=x-linalg.inv(fprime(x)).dot(f(x))
        its+=1
    if its==maxit:
        print('maximum amount of iterations ({}) reached'.format(maxit))
        print('residuum still {}'.format(linalg.norm(f(x))))
    else:
        print('newton method converged after {} iteration(s)'.format(its))
    return x

# Implicit Euler
def ImplicitEuler(t,y0,f,fy,maxit=100,tol=1e-12):
    y=[y0]
    n=array(y0).size
    for i in range(1,len(t)):
        h=t[i]-t[i-1]
        y.append(newton(lambda x: array(x)-array(y[-1])-h*f(t[i],array(x)),
            lambda x : eye(n)-h*fy(t[i],x),
            f(t[i],y[-1]),maxit,tol))
    return y

# RK4
def RK4(t,y,f):
    a=[[1/2],[0,1/2],[0,0,1]]
    b=[1/6,1/3,1/3,1/6]
    c=[1/2,1/2,1]
    return RK(a,b,c,t,y,f)

# RK4(5)
RK45adaptive = (lambda t0,y0,tmax,f,hmin,tol,rho,eta : 
    adaptive(t0,y0,tmax,f,hmin,tol,rho,eta,stepandest_rk45,4))
