k <- 10000
alpha <- 1/10
lambda <- 1
delta <- seq(1:k)
mu <- seq(1:k)
tail(delta)


n <- 30
for (i in seq(1:k)) {
  x <- rpois(n, lambda)
  mu[i] <- mean(x)
  sigma <- sqrt(mu[i]/n)
  delta[i] <- qnorm((2 - alpha)/2, mean = mu[i], sd = sigma) - mu[i]
}
res1 <- length(delta[mu - delta < 1 & 1 < mu + delta]) / length(delta)


n <- 100
for (i in seq(1:k)) {
  x <- rpois(n, lambda)
  mu[i] <- mean(x)
  sigma <- sqrt(mu[i]/n)
  delta[i] <- qnorm((2 - alpha)/2, mean = mu[i], sd = sigma) - mu[i]
}
res2 <- length(delta[mu - delta < 1 & 1 < mu + delta]) / length(delta)






