# 1 #
## a)
sum(((0:6)+1)*(7-(0:6))) # = 84

pmf_cars <- function(x) {
  out = (1/84) * (x + 1) * (7 - x)
  return(out)
}

## b)
sum(pmf_cars((4:6)))

## c) compute expectation and standard deviation
sum(pmf_cars(0:6)*(0:6)) # = 3
sum( pmf_cars((0:6)) * ((0:6)-3)^2)

# 2 #

## a) P(Tom is at least 7 x succesful)
dbinom(7, size=10, prob=0.8)

## b) P(John is at least 8 x succesful) = 1 - P(at most 7 x successful)
1 - pbinom(7, size=10, prob=0.85)

## c) P(draw)
sum(dbinom(0:10, size=10, prob=0.8) * dbinom(0:10, size=10, prob=0.85))
### this does 0 1 2 3 4 5 6 7 8 9 10
###         + 0 1 2 3 4 5 6 7 8 9 10

# 3 # see written file

# 4 #

## a)
dpois(0, 27/22)
dpois(1, 27/22)
1 - ppois(2, 27/22)

## b)
qpois(0.995, 27/22)

# 5 #
## a) Draw standard model, my = 188, sigma = 24; 188 - (+) 3*24 = 116 (260)
x <- seq(116, 260, length=10000)
y <- dnorm(x, mean = 188, sd = 24)
plot(x, y, type = "l", xlab = "cholesterol level (mg/dL)", ylab = "")

## b) What percent of adult women do you expect to have cholesterol levels over 200mg/dL?
1 - pnorm(200, mean = 188, sd = 24)

## c) What percent of adult women do you expect to have cholesterol levels between 150mg/dL and 170mg/dL?
pnorm(170, mean = 188, sd = 24) - pnorm(150, mean = 188, sd = 24)

## d) Calculate the interquartile range of the cholesterol levels.
qnorm(0.75, mean = 188, sd = 24) - qnorm(0.25, mean = 188, sd = 24)

## e) Above what value are the highest 15 %?
qnorm(0.85, mean = 188, sd = 24)















