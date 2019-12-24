import numpy as np
import math as m
from scipy import integrate as integrate
from matplotlib.pyplot import *


def gauss(f,N,T):
    Tn = np.diag([2*i+1 for i in range(N)])
    Tn = Tn + np.diag([i for i in range(1,N)],1) + np.diag([i for i in range(1,N)],-1)
    eigen = np.linalg.eig(Tn)
    values = eigen[0]
    vectors = eigen[1]

    gewicht = 1 - np.exp(-T)
    
    alphas = np.zeros(N)
    
    summe = 0
    for i in range(N):
        alphas[i] = (vectors[0][i]/np.linalg.norm(vectors[:,i]))**2*gewicht
        summe += alphas[i]*f(values[i])

    return summe

def gaussplot(f,N,T):
    Tn = np.diag([2*i+1 for i in range(N)])
    Tn = Tn + np.diag([-i for i in range(1,N)],1) + np.diag([-i for i in range(1,N)],-1)
    eigen = np.linalg.eig(Tn)
    values = eigen[0]
    vectors = eigen[1]
    
    gewicht = 1 - np.exp(-T)
    
    alphas = np.zeros(N)
    result = []
    
    summe = 0
    for i in range(N):
        alphas[i] = (vectors[0][i]/np.linalg.norm(vectors[:,i]))**2*gewicht
        
    
    return (values,alphas)




def f(x):
    return np.sin(x)

T=400
N=50


integral = 0.5

subplot(311)
x=np.linspace(1,N,N-1)
y=np.abs([integral - gauss(f,i,T) for i in range(1,N)])
title("Fehler von sin(x)")
xlabel("Stützstellen")
ylabel("Absoluter Fehler")

loglog(x,y)

x1 = np.linspace(1,N,N)
ygauss = gaussplot(f,N,T)
values = ygauss[0]
weights = ygauss[1]



subplot(312)
ylabel("Stelle der Stützstelle")
semilogy(x1,values,'rx')

subplot(313)
ylabel("Gewicht der Stützstelle")
xlabel("Aufzählung")
semilogy(x1,weights,'gx')