attach(mtcars)
par(mfrow = c(2, 1))

hist(
  rnorm(50, 5, 2),
)

hist(
  rnorm(500, 5, 2),
)