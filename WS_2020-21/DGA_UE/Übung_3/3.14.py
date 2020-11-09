import numpy as np

def verschmelzen(A, B):

    C = [0] * (len(A) + len(B))

    i = 1
    j = 1
    n = 0
    for k in range(1, len(A) + len(B) + 1):

        if j > len(B) or (i <= len(A) and A[i-1] <= B[j-1]):

            C[k-1] = A[i-1]
            i = i + 1

        else:
            n += len(A) - i + 1
            C[k-1] = B[j-1]
            j = j + 1

    return C, n

def Inversionen(A):
    if len(A) == 1:
        return A, 0
    else:
        m = int(len(A)/2)
        L = A[:m]
        R = A[m:]
        L, l = Inversionen(L)
        R, r = Inversionen(R)
        N, n = verschmelzen(L,R)
        return N, n+r+l


A = np.array([1,2,4,5,3,8,6,7])
A, a = Inversionen(A)
print(a)
