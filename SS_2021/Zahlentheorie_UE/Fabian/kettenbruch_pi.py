import math

n = 9

alpha = [(1 + math.sqrt(5)) / 2]
a = []

for i in range(0, n):
    a.append(math.floor(alpha[i]))
    alpha.append(1 / (alpha[i] - a[i]))

print(alpha)
print(a)


p = [a[0], a[1] * a[0] + 1]
q = [1, a[1]]

for i in range(2, n):
    p.append(a[i] * p[i - 1] + p[i - 2])
    q.append(a[i] * q[i - 1] + q[i - 2])

print(p)
print(q)

