data1 <- c(8.8, 10.5, 12.5, 9.7, 9.6, 13.2)
data2 <- c(8.4, 10.1, 12.0, 9.3, 9.0, 13.0)

diffs <- data1 - data2
n = 6
alpha = 0.05

diffmean = mean(diffs)
diffsd = sd(diffs)

x = diffmean/(diffsd/sqrt(n))

y = qt(1-alpha/2, n-1)

pval = pt(-x, n-1) + (1 - pt(x, n-1))