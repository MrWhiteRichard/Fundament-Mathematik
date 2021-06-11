k <- 10000
alpha <- 1/10
lambda <- 1
delta <- seq(1:k)
mu <- seq(1:k)


n <- 30
for (i in seq(1:k)) {
  x <- rpois(n, lambda)
  mu[i] <- mean(x)
  sigma <- sqrt(mu[i]/n)
  delta[i] <- - sigma * qnorm(alpha/2) 
}
res1 <- length(delta[mu - delta < 1 & 1 < mu + delta]) / length(delta)


n <- 100
for (i in seq(1:k)) {
  x <- rpois(n, lambda)
  mu[i] <- mean(x)
  sigma <- sqrt(mu[i]/n)
  delta[i] <- - sigma * qnorm(alpha/2)
}
res2 <- length(delta[mu - delta < 1 & 1 < mu + delta]) / length(delta)






