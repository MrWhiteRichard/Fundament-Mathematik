import numpy as np
from scipy.stats import unitary_group

def gen_hess(n, compl = False):
    if compl:
        a = np.random.rand(n) + np.random.rand(n)*1j
        b = np.random.rand(n-1) + np.random.rand(n-1)*1j
        c = np.random.rand(n-1) + np.random.rand(n-1)*1j
        return np.diag(b, -1) + np.diag(a,0) + np.diag(c, 1)
    else:
        a = np.random.rand(n)
        b = np.random.rand(n-1)
        c = np.random.rand(n-1)
        return np.diag(b, -1) + np.diag(a,0) + np.diag(c, 1)
    

def gen_upper_tri(eig, compl = False):
    n = eig.shape[0]
    if compl:
        return np.triu(np.random.rand(n,n) + np.random.rand(n,n) * 1j, 1) + np.diag(eig)
    else:
        return np.triu(np.random.rand(n,n),1) + np.diag(eig)
    

def gen_hermite(eig, compl = False):
    n = eig.shape[0]
    B = unitary_group.rvs(n)
    return B.T.conj()@np.diag(eig)@B


def gen_rand_mat(eig, compl = False):
    n = eig.shape[0]
    if compl:
        B = np.random.rand(n,n) + np.random.rand(n,n)*compl*1j
    else:
        B = np.random.rand(n,n)
    return np.linalg.inv(B)@np.diag(eig)@B



#print(gen_hess(5))
#print(gen_upper_tri(np.array([1,2,3]), True))
#print(gen_hermite(np.array([1,2,3,4])))
#print(gen_rand_mat(np.array([1,2,7,4])))

