x <- rbinom(5, 1, 0.5)

print(x)
print(rle(x))
print(rle(x)$lengths)