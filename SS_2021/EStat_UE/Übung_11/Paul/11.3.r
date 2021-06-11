a <- c(10, 3)
b <- c(20, 3)
c <- c(20, 1)
drange <- seq.int(-5,5,0.5)
ttest <- function(para){
  test <- mapply(function(d) (sum(replicate(1000, t.test(rnorm(para[1], 0, para[2]),
                                                         rnorm(para[1], d, para[2]), 
                                                         alternative = "two.sided",
                                                         mu = 0, paired = FALSE, var.equal = TRUE)$p.value <= 0.05))/1000), drange)
  print(test)
  return(test)
  }

plot(drange, ttest(a), xlim=c(-5,5), ylim=c(0,1), col="blue", pch=19, type="b", xlab="d", ylab="relative frequency of rejections")
points(drange, ttest(b), col="red", xlab="", ylab="", pch=19, type="b")
points(drange, ttest(c), col="orange", xlab="", ylab="", pch=19, type="b")
legend(3, 0.2, legend=c('n = 10, σ = 3', 'n = 20, σ = 3', 'n = 20, σ = 1'),
       col=c("blue", "red", "orange"), lty=1:1, cex=0.8)

# We observe that the test power is monotonously increasing in n (for fixed σ)
# and monotonously decreasing in σ (for fixed n).

