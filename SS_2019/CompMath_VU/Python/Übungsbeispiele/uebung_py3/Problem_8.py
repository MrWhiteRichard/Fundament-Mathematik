# Problem 8. A simple polynomial class


class poly:
    def __init__(self, coeff):
        self.coeff = coeff[:]

    def poly_eval(self, x):
        n = len(self.coeff)
        sum = 0
        pow = 1

        for i in range(n):
            sum += self.coeff[i] * pow
            pow *= x

        return sum

    def poly_der_coeff(self):
        n = len(self.coeff)

        if n == 1:
            return [0]
        else:
            return [self.coeff[i + 1] * (i + 1) for i in range(n - 1)]


p = poly([1, -2, 0, 0, 1, -10])

print(p.poly_eval(0))
print(p.poly_eval(1))
print(p.poly_der_coeff())
