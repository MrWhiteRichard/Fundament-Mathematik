# Computing (1 - \alpha)*100% confidence interval for \lambda 

alpha = 0.1

z = qnorm(1 - alpha/2)

calculate_confidence_interval <- function(n) {
  sample = rpois(n, lambda = 1)
  abs(mean(sample) - 1) < z*sqrt(mean(sample/n))
}

for (n in c(30, 100)) {
  percent = sum(replicate(10000, calculate_confidence_interval(n)))/100
  print(percent)
}
