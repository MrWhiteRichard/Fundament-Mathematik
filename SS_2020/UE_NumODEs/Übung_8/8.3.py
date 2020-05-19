import numpy as np

# dass die linearen Gleichungssysteme im Programm äquivalent sind zu den Gleichungen in 5.15
# muss man vermutlich noch in der Theorie aufschreiben.
# Hab alles bisher handschriftlich irgendwo hingekritzelt, latexen wird wohl zu aufwändig
# heißt, man muss es nochmal selber schön zamschreiben

def row(i,k): #Zeilenvektor Länge 2k+1
    if i == 0:
        a = np.ones(k)
        b = np.zeros(k+1)
    else:
        a = np.array([j**i for j in range(k)])
        if i == 1:
            b = np.concatenate((np.array([-1]),-1*np.ones(k)))
        else:
            b = (-i)*np.array([j**(i-1) for j in range(k+1)])
    return np.concatenate((a,b))

def AI(p,k): #Matrix Dimension p+1 x 2k+1
    A = np.zeros((p+1,2*k+1))
    for i in range(p+1):
        A[i] = row(i,k)
    return A

def AE(p,k): #Matrix Dimension p+1 x 2k
    return AI(p,k)[:,:-1]


def sol(p,k):
    return -1*np.array([k**j for j in range(p+1)])

def givehighestexp(k): #gibt array a mit alpha0,..,alphak und b mit beta0,..., betak zurück
    p = 2*k-1
    A = AE(p,k)
    if np.linalg.det(A) != 0:
        ab = np.linalg.solve(A,sol(p,k))
        a = np.append(ab[0:k] , [1]) #ak = 1
        b = np.append(ab[k:] , [0]) #bk = 0
    else:
        print("Achtung, Matrix nicht invertierbar!")
    if abs(a[0])+abs(b[0]) <= 1e-8:
        print("alpha0, beta0 Bedingung nicht erfüllt!")
        return 0

    while True: #(evtl unnötig) überprüfen, ob gefundene Koeffizienten zufällig auch Gleichung für i = 2k erfüllen
        p += 1
        err = np.dot(row(p,k)[:-1],ab) + k**p
        if np.linalg.norm(err) <= 1e-8:
            print("Höhere Konsistenzordnung als 2k-1!")
        else:
            p -= 1
            break

    return a,b,p


def givehighestimp(k):
    p = 2*k
    A = AI(p,k)
    if np.linalg.det(A) != 0:
        ab = np.linalg.solve(A,sol(p,k))
        a = np.append(ab[0:k] , [1]) #ak = 1
        b = ab[k:] #bk schon enthalten
    else:
        print("Achtung, Matrix nicht invertierbar!")

    if abs(a[0])+abs(b[0]) <= 1e-8:
        print("alpha0, beta0 Bedingung nicht erfüllt!")
        return 0
    while True:
        p += 1
        err = np.dot(row(p,k),ab) + k**p
        if np.linalg.norm(err) <= 1e-8:
            print("Höhere Konsistenzordnung als 2k!")
        else:
            p -= 1
            break

    return a,b,p

np.set_printoptions(precision = 6,suppress = True)

for i in range(2,4):
    E = givehighestexp(i)
    I = givehighestimp(i)
    print("Explizites {0}-Schritt Verfahren maximaler Ordnung {1}: alpha = {2} und beta = {3} \n".format(i,E[2],E[0],E[1]))
    print("Implizites {0}-Schritt Verfahren maximaler Ordnung {1}: alpha = {2} und beta = {3} \n".format(i,I[2],I[0],I[1]))
