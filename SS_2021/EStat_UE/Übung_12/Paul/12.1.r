mean1 = 104.23
mean2 = 62.24
n1 = 41
n2 = 49
s1 = 62.24
s2 = 16.34
alpha = 0.01

dmean = mean1 - mean2

z = dmean/sqrt(s1^2/n1 + s2^2/n2) # _H_0 ~ N(0,1)
pval = 1 - pnorm(z)# P_{H_0}(Z >= z) = 1.332083e-05 << 0.001 ???
pval

dist = qnorm(1-alpha/2)*sqrt((s1^2/n1) + (s2^2/n2))

lower = dmean - dist
upper = dmean + dist

lower
upper

