import numpy as np
import time
from scipy.stats import unitary_group

def gen_rand_mat(eig, compl = False):
    n = eig.shape[0]
    if compl:
        B = np.random.rand(n,n) + np.random.rand(n,n)*compl*1j
    else:
        B = np.random.rand(n,n)
    return np.linalg.inv(B)@np.diag(eig)@B

def gen_hess(n, compl = False):
    if compl:
        a = np.random.rand(n) + np.random.rand(n)*1j
        b = np.random.rand(n-1) + np.random.rand(n-1)*1j
        c = np.random.rand(n-1) + np.random.rand(n-1)*1j
        return np.diag(b, -1) + np.diag(a,0) + np.diag(c, 1)
    else:
        A = np.zeros((n,n))
        a = np.random.rand(n)*50
        for j in range(n-1):
            b = np.random.rand(n-j-1)*50
            A = A + np.diag(b,j+1)
        return np.diag(np.random.rand(n-1)*50, -1) + A

def gen_hermite(eig, compl = False):
    n = eig.shape[0]
    B = unitary_group.rvs(n)
    return B.T.conj()@np.diag(eig)@B

def error(eig_1, eig_2):
    eig_1 = np.sort(eig_1)
    eig_2 = np.sort(eig_2)
    eig_2 = eig_2[:len(eig_1)]
    return np.linalg.norm(eig_1 - eig_2)

def selective_error(eig_1, eig_2, k = 1):
    n_1 = len(eig_1)
    n_2 = len(eig_2)
    error_1 = np.linalg.norm(eig_1[:k] - eig_2[:k])
    error_2 = np.linalg.norm(eig_1[:n_1-k-1:-1] - eig_2[:n_2-k-1:-1])
    return error_1 + error_2

def runtime(f, A):
    start = time.time()
    S = f(A)
    end = time.time()
    return end - start

def runtime_error(f, A, eigv, k = 0, l = 0):
    if k == 0:
        l, S, count = f(A)
        S = error(S, eigv)
    else:
        l, S, count = f(lambda x: A@x, k, l)
        S = error(S, eigv)
    return count, S
