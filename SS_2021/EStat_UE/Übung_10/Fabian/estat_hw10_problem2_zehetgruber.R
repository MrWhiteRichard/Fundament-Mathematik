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
sigma <- sd(calories)
alpha <- 1/10

delta <- qnorm((2 - alpha)/2, mean = mu, sd = sigma) - mu

mu - delta
mu + delta
