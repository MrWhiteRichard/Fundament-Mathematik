alpha = 0.1

m1 = replicate(10000, mean(rpois(30, 1)))
m2 = replicate(10000, mean(rpois(100, 1)))

dist1 = m1 - qnorm(1-alpha/2)*sqrt(m1/n)
dist2 = m2 - qnorm(1-alpha/2)*sqrt(m2/n)

lower1 = m1 - dist1
lower2 = m2 - dist2

upper1 = m1 + dist1
upper2 = m2 + dist2

p1 = sum((lower1 <= 1) * (1 <= upper1))/10000
p2 = sum((lower2 <= 1) * (1 <= upper2))/10000

