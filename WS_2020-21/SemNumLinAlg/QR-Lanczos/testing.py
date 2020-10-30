import numpy as np
import generate_matrix as gm
import calc_eigvals as eig
import time


def error(eig_1, eig_2):
    return np.linalg.norm(eig_1 - eig_2)


def runtime(f,A):
    start = time.time()
    f(A)
    end = time.time()
    return end - start




# ------- testing starts here -------

n = 10
eigv = np.sort(50*np.random.rand(n)-25)
A = gm.gen_hermite(eigv)




#print(eigv)
#print(np.round(eig.QR_simple(A)[1],3))
#print(np.round(eig.QR_shift(A)[1],3))
#print(np.round(eig.QR_shift2(A)[1],3))
#print(np.round(eig.lanczos(A)[1],3))


print(error(eig.QR_simple(A)[1], eigv))
print(error(eig.QR_shift(A)[1], eigv))
print(error(eig.QR_shift2(A)[1], eigv))
print(error(eig.lanczos(A)[1], eigv))


#print(runtime(eig.QR_simple, A))
#print(runtime(eig.QR_shift, A))
#print(runtime(eig.QR_shift2, A))
#print(runtime(eig.lanczos, A))



