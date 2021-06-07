
calorie_array = c(186, 181, 176, 149, 184, 190, 158, 139, 175, 148,
                  152, 111, 141, 153, 190, 157, 131, 149, 135, 132)

n = length(calorie_array)

MLE_mu = mean(calorie_array)
MLE_sigma = mean((calorie_array - MLE_mu)^2)

alpha = 0.1

print(MLE_mu)
print(MLE_sigma)

z_alpha = qnorm(1 - alpha/2)

confidence_interval = c(MLE_mu - z_alpha*sqrt(MLE_sigma/n), MLE_mu + z_alpha*sqrt(MLE_sigma/n))

print(confidence_interval)
