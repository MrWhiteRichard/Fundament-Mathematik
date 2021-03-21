x <- c(0:6)
y1 <- (x + 1) * (7 - x)
a <- sum(y1)

y <- 1 / a * y1

b <- sum(y[5:7])

expvec <- x * y

exp <- sum(expvec)

varvec <- (x - exp)^2
var <- sum(varvec * y)
