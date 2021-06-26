library(ggplot2)

load("~/Fundament-Mathematik/SS_2021/EStat_UE/Übung_13/die.Rdata")

n = length(w)
x = as.data.frame(table(w))
colnames(x) <- c("name", "value")
x$sd = sqrt(n*(x$value/n)*(n - x$value)/n)

colors = c("blue", "orange", "red", "green")


# Most basic error bar
fig = ggplot(x) +
  geom_bar( aes(x=name, y=value), stat="identity", fill= colors , alpha=0.7) +
  geom_errorbar( aes(x=name, ymin=value-sd, ymax=value+sd), width=0.4, colour= colors, alpha=0.9, size=1.3) +
  ggtitle("Fair Die?") + xlab("Side") + ylab("Frequency") +
  theme(plot.title = element_text(hjust = 0.5))

# c)



print(chisq.test(x = x$value, p = c(1/5,2/5,1/5,1/5)))