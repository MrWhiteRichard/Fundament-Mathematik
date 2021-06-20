library(plotly)

config(.Last.value, mathjax = 'cdn')
xlab <- list(
  title = TeX("$s_1$")
)
ylab <- list(
  title = TeX("$s_2$")
)

t <- seq(0,2*pi,0.01)
x <- sqrt(55)*1.3/1.959964*cos(t)
y <- sqrt(159)*1.3/1.959964*sin(t)

fig <- plot_ly(x = x, y = y, type = 'scatter', mode = 'lines', fill = 'tozeroy', name = TeX('$\\Omega_1$'))


fig <- fig %>% layout(xaxis = xlab, yaxis = ylab)
fig <- fig %>% layout(showlegend = TRUE)
fig
