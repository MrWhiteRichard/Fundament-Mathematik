# inefficient implementation (with recursion)

def richardson_extrapolation_1(h_0, f, a, b, r):
    return recursion(h_0, f, a, b, 0, r)

def recursion(h_0, f, a, b, j, i):
    h_j = h_0/2**j

    if i == 0:
        return Q_1(h_j, f, a, b)

    else:
        tmp_1 = recursion(h_0, f, a, b, j,   i-1)
        tmp_2 = recursion(h_0, f, a, b, j+1, i-1)

        return tmp_1 + (tmp_1 - tmp_2)/(1/2**(i*2) - 1)