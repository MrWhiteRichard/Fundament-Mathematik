from Breaking_down_integers import int_break


def odd(n):
    counter = 0
    l = int_break(n)

    for i in range(len(l)):
        if l[i] % 2 == 1:
            counter += 1

    return counter


def even(n):
    counter = 0
    l = int_break(n)

    for i in range(len(l)):
        if l[i] % 2 == 0:
            counter += 1

    return counter


# only consider 8 digits after decimal point
def float_odd(x):
    x %= 1
    x *= 1e8

    return odd(int(x))


# only consider 8 digits after decimal point
def float_even(x):
    x %= 1
    x *= 1e8

    return even(int(x))


def prime_digits(n):
    primes = [2, 3, 5, 7]
    counter = 0
    l = int_break(n)

    for i in range(len(l)):
        if l[i] in primes:
            counter += 1

    return counter
