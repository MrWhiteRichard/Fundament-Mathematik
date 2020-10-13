import numpy as np
import matplotlib.pyplot as plt

#n = 2
a = 0
b = 2
n_max = 10


def beta(n):
    return n/(np.sqrt(4*n**2 - 1))

def beta_matrix(n): #initiate the matrix
    A = np.diag([beta(i) for i in range(1,n+1)],-1)
    B = np.diag([beta(i) for i in range(1,n+1)],1)
    return A+B

#A = beta_matrix(n)
#L, V = np.linalg.eig(A) #get the eigenvalues
#print_eigenvals(L, V)

def print_eigenvals(L,V): #prints eigenvalues and normed eigenvectors
    for i in range(len(L)):
        print(L[i],V[:,i])
        print("-----------------------------------------------")

def translate(x,a,b): #translates points from [-1,1] to [a,b]
    return 0.5*(a+b+x*(b-a))

def gauss_quadrature(f,n,a,b):
    L, V = np.linalg.eig(beta_matrix(n))
    sum = 0
    for i in range(len(L)):
        x = translate(L[i],a,b) #nodes on the correct intervall
        sum += f(x)*(b-a)*(V[0,i]**2)
    return sum




def test_exp(a,b,n_max):
    n_arr = [i for i in range(1,n_max)]
    err_arr = [abs(gauss_quadrature(np.exp,n,a,b) - (np.exp(b)-np.exp(a))) for n in n_arr]
    theo_err = [np.exp(b)/np.math.factorial(2*n+2)*(b-a)**(2*n+3) for n in n_arr]
    plt.semilogy(n_arr, err_arr, label = "Fehler aus Quadratur")
    plt.semilogy(n_arr, theo_err, label = "Theoretischer Fehler")
    plt.legend()
    plt.grid(linestyle = ':')
    plt.show()

def test_sin(a,b,n_max):
    n_arr = [i for i in range(1,n_max)]
    err_arr = [abs(gauss_quadrature(np.sin,n,a,b) - (np.cos(a)-np.cos(b))) for n in n_arr]
    theo_err = [1/np.math.factorial(2*n+2)*(b-a)**(2*n+3) for n in n_arr]
    plt.semilogy(n_arr, err_arr, label = "Fehler aus Quadratur")
    plt.semilogy(n_arr, theo_err, label = "Theoretischer Fehler")
    plt.legend()
    plt.grid(linestyle = ':')
    plt.show()

def test_monome(a,b,n_max,exponents):
    n_arr = [i for i in range(1,n_max)]
    for g in exponents:
        err_arr = [abs(gauss_quadrature(lambda x: x**g,n,a,b) - (b**(g+1)/(g+1)-a**(g+1)/(g+1))) for n in n_arr]
        plt.semilogy(n_arr, err_arr, label = "x^{}".format(g))
    plt.legend()
    plt.grid(linestyle = ':')
    plt.show()


test_exp(a,b,n_max)
#test_sin(a,b,n_max)
test_monome(a,b,n_max,[1,2,4,8,16])
