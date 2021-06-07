alpha = 0.1
size = 10000

m1 = replicate(size, mean(rpois(30, 1)))
m2 = replicate(size, mean(rpois(100, 1)))

dist1 = qnorm(1-alpha/2)*sqrt(m1/30)
dist2 = qnorm(1-alpha/2)*sqrt(m2/100)

lower1 = m1 - dist1
lower2 = m2 - dist2

upper1 = m1 + dist1
upper2 = m2 + dist2

p1 = sum((lower1 <= 1) * (1 <= upper1))/size
p2 = sum((lower2 <= 1) * (1 <= upper2))/size

print(p1)
print(p2)

