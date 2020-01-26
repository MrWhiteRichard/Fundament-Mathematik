import numpy as np
import time


n= 2

def vorw(L,b):
    n = len(b)

    x = np.zeros(n)

    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i][j]*x[j]
        x[i] = (b[i]-sum)/L[i][i]
    return x

def rueckw(L,b):
    n = len(b)

    x = np.zeros(n)

    for i in [n-1-k for k in range(n)]:
        sum = 0
        for j in range(i,n):
            sum += L[j][i]*x[j]  ##L transponiert ist obere Dreiecksmatrix
        x[i] = (b[i]-sum)/L[i][i]

    return x

def chol1(A):
    n = len(A)
    L = np.zeros((n,n))
    for k in range(n):
        L[k][k] = np.sqrt((A[k][k] - L[k]@L[k]))
        for i in range(k+1,n):
            L[i][k] = (A[i][k] - L[i]@L[k])/L[k][k]
    return L


def chol2(A):
     n = len(A)

     for k in range(n):
         A[k][k] = np.sqrt(A[k][k])
         A[k+1:n,k] = A[k+1:n,k]/A[k][k]
         for i in range(k+1,n):
             A[:,i] -= A[i,k]*A[:,k]  ##aufwändiger?

     return A

def chol2_unten(A):
     n = len(A)
     J = nuller(A)
     for k in range(n):
         A[k][k] = np.sqrt(A[k][k])
         A[k+1:n,k] = A[k+1:n,k]/A[k][k]
         for i in range(k+1,n):
             A[i:,i] -= A[i,k]*A[i:,k]

     for i in range(n):
         for j in range(i+1,n):
             A[i][j] = 0
     return A

def eff(n):
    A = M(n)

    start1 = time.clock()
    chol1(A)
    end1 = time.clock()

    start2 = time.clock()
    efficientChol(A)
    end2 = time.clock()

    start3 = time.clock()
    chol2_unten(A)
    end3 = time.clock()

    return end1-start1, end2-start2 #...

def M(n):

    b = np.ones(n-1)
    A = np.eye(n)*4 + np.diag(-b,1) + np.diag(-b,-1)

    c = np.ones(n**2-n)

    M = np.kron(np.eye(n,dtype=int),A) + np.diag(-c,n) + np.diag(-c,-n)

    return M

def solve(n,y):
    C = M(n)
    L = chol2(C)

    z = vorw(L,y)
    x = rueckw(L,z)

    return x, np.linalg.norm(C@np.transpose(C)@x-y)

def efficientCholBlock(n):  #Effizienz nur aus den Nullern unter A, nicht aus den in A
    A = M(n)
    L = np.zeros((n**2,n**2))
    for k in range(n**2):
        L[k][k] = np.sqrt((A[k][k] - L[k]@L[k]))
        m = min(k+n,n**2-1) #k=0 m=2
        for i in range(k+1,m+1): #1,3
             L[i][k] = (A[i][k] - L[i]@L[k])/L[k][k]

    return L


def makeN(n):
    N = np.diag(np.random.rand(n))
    r = np.random.rand(n)
    N[n-1] = r
    N[:,n-1] = r

    if (np.linalg.det(N)>0):
        M = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                M[i][j] = N[n-1-i][n-1-j]

        return N, M
    else:
        return makeN(n)


def sort(A):
    p=[]
    n = len(A)
    for i in range(n):
        j = i # Spalte, die später an die Stelle i gesetzt wird
        max = 0
        for k in range(i,n):
            c = 0
            for l in range(0,n):
                if(i != 0):
                    if(A[l][k] == 0 and A[l][i-1] == 0):
                        c += 1
                if(i == 0):
                    if(A[l][k] == 0):
                        c += 1

            if(c > max):
                max = c
                j = k

        if(i != j):
            p += [(i,j)]
        tmp = np.copy(A[:,i])
        A[:,i] = np.copy(A[:,j])
        A[:,j] = np.copy(tmp)
        tmp2 = np.copy(A[i,:])
        A[i,:] = np.copy(A[j,:])
        A[j,:] = np.copy(tmp2)
    return A, p


def nichtnuller(A):
    n = len(A)
    J = []
    for i in range(n):
        c = 0
        j = 0
        while(A[i][j] == 0):
            c += 1
            j += 1
        J += [c]
    I = []
    for k in range(n):
        Ik = []
        for j in range(k+1,n):
            if J[j] <= k:
                Ik += [j]
        I += [Ik]
    return I

def efficientChol(A):  #Effizienz nur aus den Nullern unter A, nicht aus den in A
    n = len(A)
    L = np.zeros((n,n))
    I = nichtnuller(A)
    for k in range(n):
        L[k][k] = np.sqrt((A[k][k] - L[k]@L[k]))
        for i in I[k]:
             L[i][k] = (A[i][k] - L[i]@L[k])/L[k][k]

    return L

def efffinal(N):
    L = []
    T = [2**i for i in range(2,N)]
    for n in T:
        while(True):
            C = np.zeros((n,n))
            for k in range(n):
                C[k] = np.random.rand(n)
            if(abs(np.linalg.det(C)) > 0.001):
                break
        for i in range(n):
            for k in range(n):
                if k != i and C[k][i]<(1-3.0/n):
                    C[k][i]=0
        C = C@np.transpose(C)
        #bis dahin wird nur eine random schwach besetzte pos def. symmetrische Matrix C e R^(nxn) erzeugt
        c = 0
        for i in range(n):
            for j in range(n):
                if(C[i][j] == 0):
                    c += 1
        c = c/(n*n) # prozentualer Anteil der Nuller von C

        A = np.copy(C)
        B = np.copy(C)
        start1 = time.clock()
        chol1(A)
        end1 = time.clock()
        start2 = time.clock()
        efficientChol(B)
        end2 = time.clock()
        t1 = end1-start1
        t2 = end2-start2
        L += [[n, c, t2/t1]]
    return L


print(efffinal(11))
