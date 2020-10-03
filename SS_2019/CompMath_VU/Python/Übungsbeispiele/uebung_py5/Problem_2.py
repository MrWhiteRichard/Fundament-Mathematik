import matplotlib.pylab as plt
import numpy as np


fig = plt.figure(figsize = (7.5, 5))
x = np.linspace(0, 100)


ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ax1.plot(x, 2*x, color = 'red')
ax1.set_xlabel('x')
ax1.set_ylabel('$x^2$')
ax1.legend(('$x^2$', ), loc = 2)


ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])

ax2.plot(x, 2*x, color = 'red')
ax2.set_title('zoom')
ax2.set_xlabel('x')
ax2.set_ylabel('$x^2$')
ax2.set_xlim([20, 22])
ax2.set_ylim([30, 50])


plt.show()
