#Selection Sort:
#Suche das kleinste Element und bringe es an die erste Position
#Suche das zweitkleinste und bringe es an die zweite Position
#etc. etc.

import numpy as np

def SelSort(A):
    n = len(A)
    tmp = 0
    k = 0
    for i in range(0, n-1):
        bool = 0 # ob Vertauschung ueberhaupt noetig
        min = A[i]
        for j in range(i+1, n): # min(A[i],..,A[n-1] finden)
            if A[j] < min:
                bool = 1
                min = A[j]
                k = j
        if bool == 1: # A[i] mit min vertauschen
            tmp = A[i]
            A[i] = min
            A[k] = tmp
    return A

#Bubble-Sort

def BubSort(A):
    n = len(A)
    def sorted(A): # ist A sortiert? falls (A[i],A[i+1]) Gegenbeispiel, gib [0,i] aus
        i = 0
        for i in range(n):
            if i < n-1 and (A[i] > A[i+1]):
                return 0,i
        return 1,1

    while sorted(A)[0] == 0: # Vertauschen von A[i] und A[i+1]
        i = sorted(A)[1]
        A[i], A[i+1] = A[i+1], A[i]
    return A


A = np.array([6,77,45,103,4,17])
print(SelSort(A))

A = np.array([6,77,45,103,4,17])
print(BubSort(A))
