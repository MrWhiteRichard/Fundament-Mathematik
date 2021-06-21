gamma <- 15

o1 <- c(10, 10, 20)
o2 <- c(5, 20, 5)
o3 <- c(5, 10, gamma)

n <- sum(o1) + sum(o2) + sum(o3)

e1 <- c()
e2 <- c()
e3 <- c()

for (i in seq(1:3)) {
  e1 <- c(e1, sum(o1) * (o1[i] + o2[i] + o3[i]) / n)
  e2 <- c(e2, sum(o2) * (o1[i] + o2[i] + o3[i]) / n)
  e3 <- c(e3, sum(o3) * (o1[i] + o2[i] + o3[i]) / n)
}

v <-
  sum((o1 - e1) ^ 2 / e1) + sum((o2 - e2) ^ 2 / e2) + sum((o3 - e3) ^ 2 / e3)
pchisq(v, 8, lower.tail = FALSE)
