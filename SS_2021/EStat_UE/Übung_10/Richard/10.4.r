# ---------------------------------------------------------------- #

# Create a random n Pois(lambda) sample, compute the 90% confidence interval for lambda,
# returns 1 if the confidence interval contains lambda and 0 otherwise

check_value = function(n, lambda = 1)
{
    c_sample = rpois(n, lambda)
    X_bar = mean(c_sample)
    z_alpha = qnorm(1 - 0.05)

    lower_bound = X_bar - z_alpha * sqrt(X_bar / n)
    upper_bound = X_bar + z_alpha * sqrt(X_bar / n)

    return(
        as.integer(lower_bound <= lambda & lambda <= upper_bound)
    )
}

# ---------------------------------------------------------------- #

n_1 = 30
n_2 = 100

n = 10000

print(
    sum(replicate(n, check_value(n_1))) / n * 100
)

print(
    sum(replicate(n, check_value(n_1))) / n * 100
)

# ---------------------------------------------------------------- #
