?replicate
?pexp

X <- replicate(10000, sum(rexp(10, 1/5)))

?hist

hist(X)



Y <- replicate(10000, max(rle(rbinom(50, 1, 1/2))$lengths))

mean(Y)
