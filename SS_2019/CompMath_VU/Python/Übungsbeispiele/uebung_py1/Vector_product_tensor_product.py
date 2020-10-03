def vector_prod(a, b):
    c_1 = a[1]*b[2] - a[2]*b[1]
    c_2 = a[2]*b[1] - a[0]*b[2]
    c_3 = a[0]*b[1] - a[1]*b[0]

    c = [c_1, c_2, c_3]

    return c


def tensor_prod(a, b):
    c = []

    for i in range(len(b)):
        tmp = []

        for j in range(len(a)):
            tmp.append(a[j]*b[i])

        c.append(tmp)

    return c
