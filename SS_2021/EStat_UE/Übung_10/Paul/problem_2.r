data <- c(186,181,176,149,184,190,158,139,175,148,152,111,141,153,190,157,131,149,135,132)

xbar = mean(data)
n = length(data)
s = sd(data)

alpha = 0.1
dist = qt(1-alpha/2, n-1)*(s/sqrt(n))

lower = xbar - dist
upper = xbar + dist

lower
upper