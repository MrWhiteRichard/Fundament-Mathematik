?dnorm

mu <- 5
sigma <- 2

x <- seq(0, 10, 1/100)

density_function <- dnorm(x, mu, sigma)
plot(x, density_function, type = "l")

distribution_function <- pnorm(x, mu, sigma)
plot(x, distribution_function, type = "l")



n <- 50
random_sample <- rnorm(n, mu, sigma)
hist(random_sample)

n <- 500
random_sample <- rnorm(n, mu, sigma)
hist(random_sample)

