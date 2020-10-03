import numpy as np

def saveMatrix(A):
    file = open('matrix.dat', 'w')
    strg = np.array2string(A)
    file.writelines(strg)
    file.close()

def loadMatrix():
    file = open('matrix.dat', 'r')
    strg = file.readlines()
    
    A = np.array([
            np.fromstring(strg[k][2:-2], sep = ' ')
            for k in range(len(strg))
        ])
    
    file.close()
    
    return A

    
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

saveMatrix(A)

B = loadMatrix()
print(B)
