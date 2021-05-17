dhw <- function(x, theta) { # pdf
  if (x > 1 | x < 0){
    return(0)
  } else{
    return(theta * x^(theta-1))
  }
}

phw <- function(x, theta) { # cdf
  if (0 <= x & x <= 1){
    return(x^theta)
  } else if(x > 1){
    return(1)
  } else{}
}

qhw <- function(x, theta) { # quantile function = inverse of F
  return(x^(1/theta))
}

rhw <- function(n, theta){ # random sample
  qhw(runif(n), theta)
}

sample_means = rep(0,20)
sample_sds = rep(0,20)
theor_sds = rep(0,20)
theta = 0.25

plot(NULL, xlim=c(0,10000), ylim=c(3.55,4.45), xlab="sample size", ylab="estimator")

abline(h=4, col="blue", lwd = 1)

for(i in 1:20){
  n = 500 + (i-1)*500
  sample = replicate(100, -mean(log(rhw(n, theta))))
  sample_means[i] = mean(sample)
  sample_sds[i] = sd(sample)
  theor_sds[i] = sqrt(1/(n*theta^2))

  points(rep(n,100), sample)
  points(n, sample_means[i], pch=21,bg="red",col="red")
  
  segments(n-100,4-theor_sds[i],n+100,4-theor_sds[i], col="blue", lwd = 2)
  segments(n-100,4+theor_sds[i],n+100,4+theor_sds[i], col="blue", lwd = 2)
  segments(n-100,4-sample_sds[i],n+100,4-sample_sds[i], col="red", lwd = 2)
  segments(n-100,4+sample_sds[i],n+100,4+sample_sds[i], col="red", lwd = 2)
}

legend(7500, 4.4, legend=c("Sample mean and sd", "Theoretical mean and sd"),
       col=c("red", "blue"), lty=1:1, cex=1)

