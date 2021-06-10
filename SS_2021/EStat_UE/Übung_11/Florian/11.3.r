alpha = 0.05
d_array = seq(-5,5,0.1)

two_sample_t_test <- function(n,d,sigma) {
  X = rnorm(n, mean = 0, sd = sigma)
  
  Y = rnorm(n, mean = d, sd = sigma)
  
  diff = X - Y
  
  abs(mean(diff)) > sd(diff)/sqrt(n)*qt(alpha/2, df = n - 1, lower.tail = FALSE)
}

two_sample_t_test = Vectorize(two_sample_t_test, "d")

plot(1, type = "n", xlab = "d", ylab = "Simulated power", main = "Simulated power of the two-sample t-test", xlim = c(-5,5), ylim = c(0,1))

# a)

n = 10
sigma = 3


simul_power = rowSums(replicate(1000, two_sample_t_test(n,d_array, sigma)))/1000

points(d_array, simul_power, col ="red", pch = "x")

# b)
n = 20
sigma = 3

simul_power = rowSums(replicate(1000, two_sample_t_test(n,d_array, sigma)))/1000

points(d_array, simul_power, col ="blue", pch = "x")

# c)
n = 20
sigma = 1

simul_power = rowSums(replicate(1000, two_sample_t_test(n,d_array, sigma)))/1000

points(d_array, simul_power, col ="green", pch = "x")


legend("bottomright", legend=c("n = 10, sigma = 3", "n = 20, sigma = 3", "n = 20, sigma = 1"),
       col=c("red", "blue", "green"), pch = "x")
