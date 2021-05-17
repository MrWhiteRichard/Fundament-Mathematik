
dhw <- function(x, theta){
  if (x <= 0)
    { 0 }
  else if (0 < x && x < 1)
    { theta*x^(theta - 1) }
  else
    { 0 }
}

phw <- function(x, theta){
  if (x <= 0)
    { 0 }
  else if (0 < x && x < 1)
    { x^theta }
  else
    { 1 }
}


qhw <- function(p, theta){
  stopifnot(0 <= p && p <= 1)
  p^(1/theta)
}

rhw <- function(n, theta){
  runif(n, min = 0, max = 1)^(1/theta)
}

theta = 2
sample_sizes = seq(500,10000,500)
sample_means = c()
sample_sds = c()

plot(
  1,
  type = "n",
  xlim = c(500, 10000),
  ylim = c(1/2-2/((theta)*sqrt(500)),1/2+2/((theta)*sqrt(500))),
  ylab = "estimation",
  xlab = "sample size n",
  main = paste("theta =", theta)
)

for (n in sample_sizes)
{
estimates = replicate(100, -mean(log(rhw(n, theta))))
points(replicate(100,n), estimates)
sample_means = append(sample_means, mean(estimates))
sample_sds = append(sample_sds, sd(estimates))
}



mean = 1/theta
sd = sqrt(1/(theta^2*sample_sizes))

lines(sample_sizes, replicate(length(sample_sizes), mean), col = 2, lwd = 2, lty = 2)
lines(sample_sizes,  1/2 + sd, col = 2, lwd = 2)
lines(sample_sizes,  1/2 - sd, col = 2, lwd = 2)


lines(sample_sizes, sample_means, col = 3, lwd = 2, lty = 2)
lines(sample_sizes, 1/2 + sample_sds, col = 3, lwd = 2)
lines(sample_sizes, 1/2 - sample_sds, col = 3, lwd = 2)



legend("topright", c("Theoretical Mean", "Theoretical SD", "Sample Mean", "Sample SD"), col = c(2, 2, 3, 3), lty=c(2,1,2,1), lwd = 2, cex=0.8)

