alpha = 5 * 0.01

n_array = c(10, 20, 20)
sigma_array = c(3, 3, 1)
array_length = 3

d_array = seq(-5, 5, 0.1)

simulation_number = 1000

two_sample_t_test <- function(n, d, sigma)
{
    x = rnorm(n, mean=0, sd=sigma)  
    y = rnorm(n, mean=d, sd=sigma)
    z = x - y

    t = mean(z) / (sd(z) / sqrt(n))

    t_quantile = qt(alpha/2, df=n - 1, lower.tail=FALSE)

    t_quantile < abs(t)
}

two_sample_t_test = Vectorize(two_sample_t_test, "d")

plot(
    1,
    type="n",
    xlab="d", ylab="Simulated power",
    main="Simulated power of the two-sample t-test",
    xlim=c(-5,5), ylim=c(0,1)
)

col_array <- c("red", "green", "blue")

for (i in 1:array_length)
{
    n = n_array[i]
    sigma = sigma_array[i]

    result = rowSums(
        replicate(simulation_number, two_sample_t_test(n, d_array, sigma))
    ) / simulation_number

    col = col_array[i]
    points(d_array, result, col=col, pch="x")
}
