def gauss(f,N,Tn):
    eigen = np.linalg.eig(Tn)
    values = eigen[0]
    vectors = eigen[1]
    
    alphas = np.zeros(N)
    
    summe = 0
    for i in range(N):
        alphas[i] = (vectors[0][i]/np.linalg.norm(vectors[:,i]))**2
        summe += alphas[i]*f(values[i])

    return summe
