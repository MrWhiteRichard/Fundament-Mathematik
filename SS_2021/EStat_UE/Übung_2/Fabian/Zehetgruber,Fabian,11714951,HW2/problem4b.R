lambda <- 27/22

exp(-lambda)

lambda * exp(-lambda)

x = c(0:2)

1 - sum(lambda^x / factorial(x) * exp(-lambda))

?dpois

qpois(199/200, lambda, lower.tail = TRUE)
qpois(199/200, lambda, lower.tail = FALSE)
