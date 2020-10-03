import random


def fermat(f_1, f_2):
    for n in range(2, f_1):
        a = random.randint(1, f_2)
        b = random.randint(1, f_2)
        c = random.randint(1, f_2)

        if a ** n + b ** n == c ** n:
            print('n =', n)
            print('a, b, c =', a, b, c)

            return True

    return False


def seq_x(N, n):
    if n == 0:
        return N
    else:
        tmp = seq_x(N, n-1)

        return (2 * tmp**3)/(3 * tmp**2 - 1)


def seq_y(N, n):
    if n == 0:
        return N
    else:
        tmp = seq_y(N, n-1)

        return 1/2 * (tmp + 1/tmp)
