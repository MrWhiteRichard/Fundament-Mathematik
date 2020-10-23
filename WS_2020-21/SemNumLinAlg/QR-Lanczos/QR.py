import numpy as np
from scipy.linalg import block_diag


tol = 1e-16
B = np.random.rand(5,5)
A_1 = np.array([[1,4,6,7,8],[0,10,6,8,9],[0,0,100,8,9],[0,0,0,1000,5],[0,0,0,0,10000]])
A_2 = np.array([[1,4,6,7,8],[0,1.01,6,8,9],[0,0,1.02,8,9],[0,0,0,1.03,5],[0,0,0,0,1.04]])
B_inv = np.linalg.inv(B)

A_1 = B_inv@A_1@B
A_2 = B_inv@A_2@B

def QR_simple(A,tol):
    i = 0
    while abs(A[1,0]) > tol:
        Q,R = np.linalg.qr(A)
        A = R@Q
        i +=1
    print(i)
    return A, np.diag(A)

def QR_shift(A,tol):
    m = A.shape[1]
    i = 0
    for n in range(m-1,0,-1):
        while abs(A[n,n-1]) > tol:
            rho = A[n,n]
            Q,R = np.linalg.qr(A-rho*np.identity(m))
            A = R@Q + rho*np.identity(m)
            i +=1
        A[n,:n-m] = 0
    print(i)
    return A, np.diag(A)

def QR_shift2(A,tol):
    m = A.shape[1]
    i = 0
    for n in range(m-1,0,-1):
        while abs(A[n,n-1]) > tol*(abs(A[n-1,n-1])+abs(A[n,n])):
            w = np.linalg.eigvals(A[n-1:n+1,n-1:n+1])
            if abs(w[0] - A[n,n]) < abs(w[1] - A[n,n]):
                rho = w[0]
            else:
                rho = w[1]
            Q,R = np.linalg.qr(A-rho*np.identity(m))
            A = R@Q + rho*np.identity(m)
            i += 1
        A[n,:n-m] = 0
    print(i)
    return A, np.diag(A)


def Lanczos(A):
    n = A.shape[1]
    v0 = np.random.rand(n)
    v = [v0/np.linalg.norm(v0)]
    gam = [v[0].T@A@v[0]]
    w = (A - gam[0]*np.identity(n))@v[0]
    delta = [np.linalg.norm(w)]
    j = 0
    while delta[j] > 1e-5 and j < 100:
        print(delta[j])
        v.append(w/delta[j])
        j +=1
        gam.append(v[j].T@A@v[j])
        w = (A - gam[j]*np.identity(n))@v[j] - delta[j-1]*v[j-1]
        delta.append(np.linalg.norm(w))
    T = np.diag(delta[:-1], -1) + np.diag(gam) + np.diag(delta[:-1], 1)
    return QR_shift(T)

#Matrix, EV = QR_simple(A_1,tol)
#Matrix, EV = QR_shift(A_1,tol)
#Matrix, EV = QR_shift2(A_1,tol)
#Matrix, EV = QR_simple(A_2,tol)
#Matrix, EV = QR_shift(A_2,tol)
#Matrix, EV = QR_shift2(A_2,tol)


#print(np.round(Matrix.real,2))
#print(EV.real)


A = np.diag([1,1,1], -1) + np.diag([2,2,2,2]) + np.diag([3,3,3], 1)

def QR_decomp_hesse(A):
    n = A.shape[0]
    Q = np.eye(n,n)

    for i in range(0,n-1):
#        root = (abs(A[i,i])**2+abs(A[i+1,i])**2)**(1/2)
#        c = A[i,i]/root
#        s = A[i+1,i]/root
        if abs(A[i,i]) >= abs(A[i+1,i]):
            t = A[i+1,i]/abs(A[i,i])
            root = (1+abs(t)**2)**(1/2)
            c = A[i,i]/(abs(A[i,i])*root)
            s = t/root
        else:
            t = A[i,i]/abs(A[i+1,i])
            root = (1+abs(t)**2)**(1/2)
            s = A[i+1,i]/(abs(A[i+1,i])*root)
            c = t/root

        M = np.array([[c.conj(), s.conj()], [-s, c]])
        G = block_diag(np.eye(i,i), M, np.eye(n-i-2, n-i-2))
        Q = G@Q
#        print(G)
        for j in range(i, n):
            temp_1 = A[i,j]
            A[i,j] = c.conj()*temp_1 + s.conj()*A[i+1,j]
            A[i+1,j] = -s*temp_1 + c*A[i+1,j]

    return Q.T, A

Q,R = QR_decomp_hesse(A)
print(np.round(Q,3))
print(np.round(R,3))
print(np.round(Q@R,3))
