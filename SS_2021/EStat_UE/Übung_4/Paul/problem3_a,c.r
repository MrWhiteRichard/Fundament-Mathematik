## Problem 4
## For part (b), see pdf

x <- seq(-10, 15, by = 0.001)
cdf <- pnorm(x, mean = 5, sd = 2)
plot(x, cdf, xlim = c(-10,15), ylim = c(0,1), xlab = "x", ylab = "value of pdf")

pdf <- dnorm(x, mean = 5, sd = 2)
plot(x, pdf, xlim = c(-10,15), ylim = c(0,0.2), xlab = "x", ylab = "value of cdf")

hist(rnorm(50,5,2))

hist(rnorm(500,5,2))
