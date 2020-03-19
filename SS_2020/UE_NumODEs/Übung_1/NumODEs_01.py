import numpy as np
import matplotlib.pyplot as plt

# maximale Anzahl der Zerlegungspunkte
n_max = 100

# exakte Lösung zum Endzeitpunkt t = 1
y_exact = np.sqrt(np.exp(1))

# Fehler zum Endzeitpunkt
epsilon = []

for n in range(1, n_max):

    # Rekurstions-Anfang
    y_approx = [1]

    # Rekursions-Schritt(e)
    for i in range(n):
        y_approx += [y_approx[-1] + i/n**2 * y_approx[-1]]

    epsilon += [abs(y_exact - y_approx[-1])]

# Anzahlen der Zerlegungspunkte
n = np.array(range(1, n_max))

# plotten
plt.loglog(n, epsilon, label = "$\epsilon(n)$")
plt.loglog(n, 1/n,     label = "$\mathcal{O}(n^{{-1}})$")
plt.xlabel("Anzahl der Zerlegungspunkte ($n$)")
plt.legend()
plt.grid(linestyle = ':')
plt.savefig('Fehler zum Endzeitpunkt vs. Anzahl der Zerlegungspunkte' + '.png')
plt.show()
