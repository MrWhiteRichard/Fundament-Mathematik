new <- c(80,76,70,80,66,85,79,71,81,76)
old <- c(79,73,72,62,76,68,70,86,75,68,73,66)

m1 = mean(new)
m2 = mean(old)
n1 = length(new)
n2 = length(old)
s1 = sd(new)
s2 = sd(old)
alpha = 0.05

nu = ((s1^2/n1)+(s2^2/n2))^2 / ( ((s1^2/n1)^2/(n1-1)) + ((s2^2/n2)^2/(n2-1)) )
dist = qt(1-alpha/2, nu) * sqrt(s1^2/n1+s2^2/n2)
lower = m1 - m2 - dist
upper = m1 - m2 + dist

print(lower)
print(upper)

hist(old)
hist(new)
