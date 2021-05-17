?runif

dhw <-
  function(x, theta)
    ifelse(x <= 0 | x >= 1, 0, theta * x ^ (theta - 1))
dhw(-2, 2)

phw <-
  function(x, theta)
    ifelse(x <= 0, 0, ifelse(x >= 1, 1, x ^ theta))
phw(1 / 2, 3)

qhw <- function(p, theta)
  return(p ^ (1 / theta))
qhw(phw(1 / 4, 5), 5)

rhw <- function(n, theta)
  return(qhw(runif(n), theta))
rhw(4, 2)

S <- function(x) {
  -mean(log(x))
}
x <- c(1, 4, 3)
S(x)


theta <- 2
sample_size <- seq(500, 10000, 500)
theoretical_mu <- 1 / theta
theoretical_sigma500 <- 1 / (sqrt(500) * theta)
plot(
  1,
  type = "n",
  xlim = c(500, 10000),
  ylim = c(
    theoretical_mu - 2 * theoretical_sigma500,
    theoretical_mu + 2 * theoretical_sigma500
  ),
  ylab = "estimation",
  xlab = "sample size n",
  main = paste("theta =", theta)
)



for (n in sample_size) {
  est <- replicate(100, S(rhw(n, theta)))
  mu <- mean(est)
  sigma <- sd(est)
  points(replicate(100, n), est)
  arrows(
    n,
    mu - sigma,
    n,
    mu + sigma,
    length = 0.1,
    angle = 90,
    code = 3,
    col = "red"
  )
  points(n, mu, col = "red", pch = 19)
  theoretical_sigma <- 1 / (sqrt(n) * theta)
  arrows(
    n,
    theoretical_mu - theoretical_sigma,
    n,
    theoretical_mu + theoretical_sigma,
    length = 0.1,
    angle = 90,
    code = 3,
    col = "green"
  )
}

lines(
  c(0, sample_size, 10500),
  replicate(length(sample_size) + 2, theoretical_mu),
  col = "green",
  lwd = 2
)

