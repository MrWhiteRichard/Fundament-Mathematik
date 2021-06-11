calories <-
  c(
    186,
    181,
    176,
    149,
    184,
    190,
    158,
    139,
    175,
    148,
    152,
    111,
    141,
    153,
    190,
    157,
    131,
    149,
    135,
    132
  )

mu <- mean(calories)
n <- length(calories)
sigma <- sqrt(1/ (n - 1) * sum((calories - mu)^2))
alpha <- 1/10

delta <- - sigma / sqrt(n) * qnorm(alpha/2)

mu - delta
mu + delta
