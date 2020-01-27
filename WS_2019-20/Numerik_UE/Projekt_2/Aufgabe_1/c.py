import numpy as np
import time
import matplotlib.pyplot as plt

class Sparse:

    def __init__(self,b,v, J = np.zeros(0), I = np.zeros(0)):
        if b:
            self.v = np.array(v)
            self.J = np.array(J)
            self.I = np.array(I)
            self.n = len(self.I)-1
        else:
            self.v, self.J, self.I = self.fromdense(v)
            self.n = len(self.I)-1

    def __matmult__(self,b):
        d = np.zeros(self.n)
        for i in range(self.n):
            x = np.array(self.J[self.I[i]:self.I[i+1]]).astype(int)
            d[i] = self.v[self.I[i]:self.I[i+1]]@b[x]
        return d


    def todense(self):
        A = np.zeros([self.n,self.n])
        for i in range(self.n):
            for j in range(self.I[i],self.I[i+1]):
                A[i][self.J[j]] = self.v[j]
        return A

    def fromdense(self,A):
        v,J = np.zeros(0), np.zeros(0)
        I = np.array([0])
        c = 0
        for i in range(np.shape(A)[0]):
            x = np.where(A[i] != 0)
            v = np.append(v,A[i][x])
            for j in x:
                J = np.append(J,x)
            c += len(x[0])
            I = np.append(I,c)
        return v, J.astype(int), I

def cg(A,b,x0,tol):
    xt = x0
    r0 = b - np.dot(A,xt)
    d = r0
    while(np.linalg.norm(r0) > tol):
        prod = np.dot(np.transpose(r0),r0)
        prod2 = np.dot(A,d)
        alpha = prod/np.dot(np.transpose(d),prod2)
        xt = xt + alpha*d
        r0 = r0 - alpha*prod2
        beta = np.dot(np.transpose(r0),r0)/prod
        d = r0 + beta*d
    return xt


def vcg(A,b,x0,P,tol):
    r0 = b - A.__matmult__(x0)
    P_inv = np.linalg.inv(P)
    z0 = P_inv@r0
    d = z0
    c = 0
    while(np.linalg.norm(r0) > tol):
        prod = np.dot(np.transpose(z0),r0)
        prod2 = A.__matmult__(d)
        alpha = np.dot(np.transpose(r0),z0)/np.dot(np.transpose(d),prod2)
        x0 = x0 + alpha*d
        r0 = r0 - alpha*prod2
        z0 = P_inv@r0
        beta = np.dot(np.transpose(z0),r0)/prod
        d = z0 + beta*d
        c += 1
    return x0

def Scg(A,b,x0,tol):
    xt = x0
    r0 = b - A.__matmult__(xt)
    d = r0
    while(np.linalg.norm(r0) > tol):
        prod = np.dot(np.transpose(r0),r0)
        prod2 = A.__matmult__(d)
        alpha = prod/np.dot(np.transpose(d),prod2)
        xt = xt + alpha*d
        r0 = r0 - alpha*prod2
        beta = np.dot(np.transpose(r0),r0)/prod
        d = r0 + beta*d
    return xt


if __name__ == "__main__":
    x = Sparse(True, [1,2,3,4,5,6],[2,0,1,0,4,4],[0,1,3,5,5,6])

    n = 14000
    z = 20
    b = np.random.rand(n)
    x0 = np.random.rand(n)
    tol = 10**-10
    A = np.zeros((n,n))
    start = time.process_time()
    for i in range(n):
        non_zeros = np.random.rand(z)
        zeros = np.zeros(n-z)
        A[i] = np.concatenate((non_zeros, zeros))
        np.random.shuffle(A[i])
    A = A + A.T + np.diag(np.random.rand(n)*1000)
    end = time.process_time()
    print("Random-Erstellungszeit: {}".format(end-start))
    start = time.process_time()
    xt1 = cg(A,b,x0,tol)
    end = time.process_time()
    print("Standard-cg-Rechenzeit: {}".format(end - start))
    start = time.process_time()
    A = Sparse(False, A)
    end = time.process_time()
    print("Konvertierungszeit: {}".format(end - start))
    start = time.process_time()
    xt2 = Scg(A,b,x0, tol)
    end = time.process_time()
    print("Sparse-cg-Rechenzeit: {}".format(end - start))
    print(np.linalg.norm(A.__matmult__(xt1)-b),np.linalg.norm(A.__matmult__(xt2)-b))