import math


def replace_string(s_in, s_find, s_replace):
    sentence = s_in.split()

    for i in range(len(sentence)):
        if sentence[i] == s_find:
            sentence[i] = s_replace

    s_out = sentence[0]

    for i in range(1, len(sentence)):
        s_out += " " + sentence[i]

    return s_out


sentence_1 = "Wisse, Rotkraut bleibt Rotkraut und Brautkleid bleibt Brautkleid."
sentence_2 = replace_string(sentence_1, "Rotkraut", "Blaukraut")
print(sentence_2)


def remove_spaces(sentence, capitalise=False):
    new_sentence = ""

    for letter in sentence:
        if letter != " ":
            new_sentence += letter

    if capitalise:
        new_sentence = new_sentence.upper()

    return new_sentence


xkcd = "A solar plexus says what?"
print(remove_spaces(xkcd))


class Complex:
    def __init__(self, z1, z2):
        self.z1 = z1
        self.z2 = z2

    def add(self):
        real = self.z1[0] + self.z2[0]
        imag = self.z1[1] + self.z2[1]

        z = (real, imag)
        return z

    def multiply(self):
        real = self.z1[0] * self.z2[0] - self.z1[1] * self.z2[1]
        imag = self.z1[0] * self.z2[1] + self.z1[1] * self.z2[0]

        z = (real, imag)
        return z

    def divide(self):
        real = self.z1[0] * self.z2[0] + self.z1[1] * self.z2[1]
        real /= self.z2[0] ** 2 + self.z2[1] ** 2

        imag = self.z1[1] * self.z2[0] - self.z1[0] * self.z2[1]
        imag /= self.z2[0] ** 2 + self.z2[1] ** 2

        z = (real, imag)
        return z


z1 = (1, 0)
z2 = (0, 1)

Obj = Complex(z1, z2)

print(Obj.add())
print(Obj.multiply())
print(Obj.divide())


class Vector:
    def add(self, z1, z2):
        z = []

        for i in range(len(z1)):
            z += [z1[i] + z2[i]]

        return z

    def scalar(self, a, z1):
        z = []

        for zi in z1:
            z += [a * zi]

        return z


class VectorPlus(Vector):
    def vector_prod(self, z1, z2):
        z = []

        z += [z1[1] * z2[2] - z1[2] * z2[1]]
        z += [z1[2] * z2[0] - z1[0] * z2[2]]
        z += [z1[0] * z2[1] - z1[1] * z2[0]]

        return z

    def tensor(self, z1, z2):
        Z = []

        for j in range(len(z1)):
            tmp = []

            for i in range(len(z2)):
                tmp += [z1[j] * z2[i]]

            Z += [tmp]

        return Z


Obj = VectorPlus()

print(Obj.add([1, 2, 3, 4], [5, 6, 7, 8]))
print(Obj.scalar(2, [1, 2, 4, 8]))
print(Obj.vector_prod([1, 0, 0], [0, 1, 0]))
print(Obj.tensor([1, 2, 3, 4], [1, 2, 3, 4]))


class faculty:
    def fac(self, n, ptr=False):
        fac = math.factorial(n)

        if ptr:
            print(fac)

        return fac

    def fac_stir(self, n, ptr=False):
        fac = math.sqrt(2 * math.pi * n) * (n / math.e) ** n

        if ptr:
            print(fac)

        return fac

    def fac_gam(self, n, ptr=False):
        fac = math.sqrt(2 * math.pi / (n - 1)) * (1 / math.e * ((n - 1) + 1 / (12 * (n - 1) - 1 / (10 * (n - 1))))) ** (
                n - 1)

        if ptr:
            print(fac)

        return fac

    def fac_stir_err(self, n, ptr=False):
        fac = abs(self.fac_stir(n) - self.fac(n))

        if ptr:
            print(fac)

        return fac

    def fac_gam_err(self, n, ptr=False):
        fac = abs(self.fac_gam(n) - self.fac(n))

        if ptr:
            print(fac)

        return fac


Obj = faculty()
n = 4

print(Obj.fac(n))
print(Obj.fac_stir(n))
print(Obj.fac_gam(n))
print(Obj.fac_stir_err(n))
print(Obj.fac_gam_err(n))


def dec(ev, fun):
    def inner():
        return fun(ev)

    return inner


f = dec(1, math.exp)
g = dec(4, math.gamma)

print(f())
print(g())


def comp(fun1, fun2, fun3):
    def inner(n):
        return fun1(fun2(fun3(n)), n)

    return inner


def fun1(x, n):
    return x ** n


def fun2(x):
    return 1 + x


def fun3(n):
    return 1 / n


exp_approx = comp(fun1, fun2, fun3)
print(exp_approx(1000))


def count(func):
    counter = 0

    def inner(x):
        nonlocal counter
        counter += 1
        return counter, func(x)

    return inner


f = count(math.sin)

for i in range(4):
    print(f(math.pi / 2 * i))


def ompalompa(x, y):
    if abs(y) < 1e-14:
        raise ZeroDivisionError("division by (almost) zero")
    else:
        return x/y


print(ompalompa(1, 1))
print(ompalompa(0, 1))

x = ompalompa(1, 1e-13)
x = ompalompa(1, 0)
