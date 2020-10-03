import math


def int_break(n):
    digit_amount = int(math.log10(n)) + 1

    l = []

    for i in range(digit_amount):
        l.append(n % 10)
        n //= 10

    return l


def counter(n):
    l = int_break(n)
    k = []

    for i in range(len(l)):
        k.append(l[len(l) - i - 1])

    return k
