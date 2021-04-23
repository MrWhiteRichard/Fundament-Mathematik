print(
    mean(
        replicate(
            n = 10000,
            max(
                rle(rbinom(50, 1, 0.5))$lengths
            )
        )
    )
)