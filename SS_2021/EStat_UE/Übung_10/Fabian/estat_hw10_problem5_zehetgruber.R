setwd("Documents/Fundament-Mathematik/SS_2021/EStat_UE/Übung_10/Fabian")
load("../algorithms.Rdata")

boxplot(
  runningtimes,
  ylab = "runningtime",
  main = "runningtimes of two algorithms",
  col = "green",
  border = "blue"
)
