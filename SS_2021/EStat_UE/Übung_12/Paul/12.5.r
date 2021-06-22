alpha = 0.05
before <- c(10, 16, 7, 4, 7, 2)
after <- c(18, 19, 11, 3, 5, 3)
diffs <- before - after
n = length(diffs)

z = mean(diffs)/(sd(diffs)*sqrt(n))

zz = qt(0.05, n-1)

print(z)
print(zz)

hist(before)
hist(after)
