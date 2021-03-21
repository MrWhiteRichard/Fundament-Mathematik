?dnorm

mu <- 188
sigma <- 24


x <- seq(100, 300, 1/2)

bell <- dnorm(x, mu, sigma)

plot(x, bell, type = "l", xlab = "cholesterol level [mg/dL]", ylab = "probability density")

pnorm(200, mu, sigma, lower.tail = FALSE)
1 - pnorm(150, mu, sigma, lower.tail = TRUE) - pnorm(170, mu, sigma, lower.tail = FALSE)

qnorm(75/100, mu, sigma) - qnorm(25/100, mu, sigma)

qnorm(15/100, mu, sigma, lower.tail = FALSE)
