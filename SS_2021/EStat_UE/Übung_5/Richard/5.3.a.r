hist(
    replicate(
        n = 10000,
        sum(rexp(10, rate = 0.2))
    )
)