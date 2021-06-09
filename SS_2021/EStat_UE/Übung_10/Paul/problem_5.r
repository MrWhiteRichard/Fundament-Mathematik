setwd("/home/paul/documents/Fundament-Mathematik/SS_2021/EStat_UE/Übung_10/Paul")
x <- get(load("algorithms.Rdata"))
boxplot(x, horizontal=TRUE, range=0, col=c("blue", "green"), xlab = "running time (in seconds)", main = "Running times of algoA vs. algoB")

# b)

## The first quartile of the times in A was about? -- 20
## the interquartile range of the times in B is about twice the interquartile range of A -- A has IQR ca. 12, B has IQR ca. 24, so yes
## Is n = 100? -- This information is not contained within the boxplots.
## More than half of the running times in B were faster than 3/4 of the running times in A. -- False, it could be exactly 1/2.
## At least 50% in A were faster than the 25% slowest in B. -- True
## At least 60% in A were faster than the 25% slowest in B. -- We can't decide that from the boxplots.
