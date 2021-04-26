## Problem 3

# a)
hist(replicate(10000, sum(rexp(10, rate=0.2))))

# We expect the histogram to look like the density of a
# Gamma(n, l)-distributed r.v., were n = 10 and l = 0.2.


# b)
mean(replicate(10000, max(unlist(rle(rbinom(50, 1, 0.5))[1]))))
     
# The results were slightly below 6.
