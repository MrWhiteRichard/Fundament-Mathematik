
x <- seq(1,9,0.01)

plot(x,dnorm(x,5,2), type = "l", col = "black", lwd = 2, xlab = "x", ylab = "f(x)", main = "Probability Density Function (pdf)")

plot(x,pnorm(x,5,2), type = "l", col = "black", lwd = 2, xlab = "x", ylab = "F(x)", main = "Cummulative Distribution Function (cdf)")

bell <- rnorm(50,5,2)

hist(bell)

bell <- rnorm(500,5,2)

hist(bell)