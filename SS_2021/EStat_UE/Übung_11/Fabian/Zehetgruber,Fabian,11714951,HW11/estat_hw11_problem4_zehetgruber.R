m1 <- 5275
s1 <- 150
m2 <- 5240
s2 <- 200
n1 <- 400
n2 <- 400

h1 <- s1 ^ 2 / n1
h2 <- s2 ^ 2 / n2

mu_hat <- m1 - m2

# a) 95% confidence interval
c(mu_hat + qnorm(alpha / 2) * sqrt(h1 + h2),
  mu_hat - qnorm(alpha / 2) * sqrt(h1 + h2))

# b) two-sided p-value 0
2 * pnorm(-mu_hat / sqrt(h1 + h2))

# c) one-sided p-value 0

pnorm(-mu_hat / sqrt(h1 + h2))

# d) two-sided p-value 25
2 * pnorm(-(mu_hat - 25) / sqrt(h1 + h2))
