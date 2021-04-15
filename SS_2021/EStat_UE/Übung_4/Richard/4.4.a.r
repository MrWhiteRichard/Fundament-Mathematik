x <- seq(-10, 10, by = 0.2)

attach(mtcars)
par(mfrow = c(2, 1))

y <- dnorm(x, mean = 5, sd = 2)
plot(x, y, type = "l", col = "black", lwd = 2, xlab = "x", ylab = "f(x)", main = "Probability Density Function (pdf)")

y <- pnorm(x, mean = 5, sd = 2)
plot(x, y, type = "l", col = "black", lwd = 2, xlab = "x", ylab = "F(x)", main = "Cummulative Distribution Function (cdf)")