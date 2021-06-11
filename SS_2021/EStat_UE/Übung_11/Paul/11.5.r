hs <- c(131, 74, 129, 96, 92)
hf <- c(44, 70, 69, 43, 53)
fb <- c(15, 14, 21, 29, 21)
alpha = 0.05
n = 5

# a)
s1 = sd(hs)
s2 = sd(hf)

nu = ((s1^2+s2^2)/n)^2 / (((s1^2/n)^2 + (s2^2/n)^2)/ (n-1))
dist = qt(1-alpha/2, nu) * sqrt((s1^2+s2^2)/n)
lower = mean(hs) - mean(hf) - dist
upper = mean(hs) - mean(hf) + dist

print(lower)
print(upper)

# b)
s1 = sd(hf)
s2 = sd(fb)

nu = ((s1^2+s2^2)/n)^2 / (((s1^2/n)^2 + (s2^2/n)^2)/ (n-1))
dist = qt(1-alpha/2, nu) * sqrt((s1^2+s2^2)/n)
lower = mean(hf) - mean(fb) - dist
upper = mean(hf) - mean(fb) + dist

print(lower)
print(upper)
