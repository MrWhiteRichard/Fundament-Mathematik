n1 <- 41
n2 <- 49

mu1 <- 104.23
mu2 <- 62.24

s1 <- 62.24
s2 <- 16.34

alpha <- 1 / 100

s <- sqrt(s1 ^ 2 / n1 + s2 ^ 2 / n2)

1 - pnorm((mu1 - mu2) / s)

c(mu1 - mu2 + s * qnorm(alpha / 2), mu1 - mu2 - s * qnorm(alpha / 2))
