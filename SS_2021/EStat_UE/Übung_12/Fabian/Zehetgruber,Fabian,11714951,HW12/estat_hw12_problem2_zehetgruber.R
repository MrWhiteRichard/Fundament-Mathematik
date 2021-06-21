meth1 <- c(80, 76, 70, 80, 66, 85, 79, 71, 81, 76)
meth2 <- c(79, 73, 72, 62, 76, 68, 70, 86, 75, 68, 73, 66)

t.test(meth1, meth2)
t.test(meth1, meth2, var.equal = TRUE)

sd(meth1) ^ 2
sd(meth2) ^ 2

hist(meth1)
hist(meth2)
?hist
