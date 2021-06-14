handshake <- c(131, 74, 129, 96, 92)
high_five <- c(44, 70,  69, 43, 53)
fist_bump <- c(15, 14,  21, 29, 21)

n <- 5

mu1 <- mean(handshake)
s1 <- sd(handshake)
mu2 <- mean(high_five)
s2 <- sd(high_five)
mu3 <- mean(fist_bump)
s3 <- sd(fist_bump)

h1 <- s1 ^ 2 / n
h2 <- s2 ^ 2 / n
h3 <- s3 ^ 2 / n

nu1 <- (h1 + h2) ^ 2 / (h1 ^ 2 / (n - 1) + h2 ^ 2 / (n - 1))
alpha <- 1 / 20

# a) 95% confidence interval: handshake - high_five
nu1 <- (h1 + h2) ^ 2 / (h1 ^ 2 / (n - 1) + h2 ^ 2 / (n - 1))
c(mu1 - mu2 + qt(alpha / 2, nu1) * sqrt(h1 + h2),
  mu1 - mu2 - qt(alpha / 2, nu2) * sqrt(h1 + h2))

# b) 95% confidence interval: high_five - fist_bump
nu2 <- (h2 + h3) ^ 2 / (h2 ^ 2 / (n - 1) + h3 ^ 2 / (n - 1))
c(mu2 - mu3 + qt(alpha / 2, nu2) * sqrt(h2 + h3),
  mu2 - mu3 - qt(alpha / 2, nu2) * sqrt(h2 + h3))
