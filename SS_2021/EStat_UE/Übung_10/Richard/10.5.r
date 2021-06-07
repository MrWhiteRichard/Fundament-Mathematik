load("SS_2021//EStat_UE//Übung_10//algorithms.Rdata")

boxplot(
    runningtimes,
    ylab = "Runtime in seconds",
    col = c("red", "blue"),
    main = "Runtimes of algoA and algoB respectively"
)
