n1 <- 55
n2 <- 159

xbar1 <- 8.2
xbar2 <- 6.9

alpha <- 1 / 20

smax <- (xbar1 - xbar2) / qnorm(1 - alpha)

s <- -(xbar1 - xbar2) / qnorm(alpha / 2)