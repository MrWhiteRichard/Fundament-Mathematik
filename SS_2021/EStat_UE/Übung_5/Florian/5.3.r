bell <- replicate(10000,sum(rexp(10,0.2)))

hist(bell, main = "Histogramm of X1+...+X10")

runlengths <- rle(rbinom(50,1,0.5))

longestruns <- replicate(10000, max(rle(rbinom(50,1,0.5))$lengths))

print(mean(longestruns))
