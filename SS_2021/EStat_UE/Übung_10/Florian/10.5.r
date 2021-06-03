load("algorithms.rData")

boxplot(runningtimes, ylab = "Runtime in seconds", col = c("red", "blue"), main = "Runtimes of AlgoA and AlgoB")

# a) first quartile of times in A: ~ 20
# b) The interquartile range of the times in B is about trice the interquartile range of A: I would say about twice.
# c) Is n = 100? Can't tell from the boxplot alone.
# d) More then half of the running times in B were faster then 3/4 of the running times in A: Yes.
# e) At least 50% in A were faster than the 25% slowest in B: Yes.
# f) At least 60% in A were faster than the 25% slowest in B: Can't tell from the boxplot alone.