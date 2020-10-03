import matplotlib.pylab as plt
import numpy as np

fig = plt.figure(figsize = (5, 7.5))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

x = np.linspace(0, 100)
y = np.linspace(0, 200)

ax.plot(x, y)
plt.xlabel('x')
plt.legend(('a line', ), loc = 'upper center')
plt.title('title')

plt.show()
