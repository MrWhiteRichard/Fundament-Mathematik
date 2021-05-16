
dhw <- function(x, theta){
  theta*x^(theta - 1)
}

phw <- function(x, theta){
  x^theta
}


qhw <- function(p, theta){
  p^(1/theta)
}

rhw <- function(n, theta){
  runif(n, min = 0, max = 1)^(1/theta)
}


theta = 2
estimates = c()
sample_means = c()
samples = c()
sample_sizes = seq(500,10000,500)
for (n in sample_sizes)
{samples = append(samples, rhw(500, theta))
Sn = sum(-1/n*log(samples))
estimates = append(estimates, Sn)
sample_mean = 1/n*sum(estimates)*500
sample_means = append(sample_means, sample_mean)

}

plot(sample_sizes, estimates, col = 1, type = "p", xlab = "Sample size", ylab = "y", ylim = c(0.4,0.8))
points(sample_sizes, sample_means, col = 2)
abline(0.5,0, col = 1)
abline(2/3,0, col = 2)

sd = sqrt(theta^2/sample_sizes)

lines(sample_sizes,  2/3 + sd, col = 3)
lines(sample_sizes,  2/3 - sd, col = 3)

legend("topright", c("Estimates of 1/theta", "Sample means"), col = c(1,2), lty=1, cex=0.8)

