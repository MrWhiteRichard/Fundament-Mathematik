## a)
x1 = 5275
x2 = 5240
s1 = 150
s2 = 200
alpha = 0.05
n = 400

dist = qnorm(1-alpha/2)*sqrt((s1^2+s2^2)/n)
lower = x1 - x2 - dist
upper = x1 - x2 + dist
lower
upper

## b)
z = (x1 - x2)/(sqrt((s1^2+s2^2)/n))
z
qnorm(1-alpha/2)
2*pnorm(-z)

## c)
1-pnorm(z)

## d)
z = (x1 - x2 - 25)/(sqrt((s1^2+s2^2)/n))
z
2*pnorm(-z)
