n <- 6
x <- c(8.8,
       10.5,
       12.5,
       9.7,
       9.6,
       13.2)
y <- c(8.4,
       10.1,
       12.0,
       9.3,
       9.0,
       13.0)
d <- x - y
mu_d <- mean(d)
sigma_d <- sqrt(1 / (n - 1) * sum((d - mu_d) ^ 2))

1 - pt(mu_d * sqrt(n) / sigma_d, n - 1)
