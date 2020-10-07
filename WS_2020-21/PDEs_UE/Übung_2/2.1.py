import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

fig = plt.figure()

x = np.arange(-6, 6, 0.1)

y = np.arange(-6, 6, 0.1)

xx, yy = np.meshgrid(x, y)
z = xx**2 - 9*(yy**2+1)
levels = [-100,-50,-10,-5,0,5,10,50,100]
cp = plt.contourf(x,y,z, levels = levels, cmap='RdYlGn')
levels = [-1000000,0,10000000]
CS = plt.contour(x,y,z, levels = levels, colors='k')
plt.clabel(CS, inline=1, fontsize=10)
fig.colorbar(cp)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

fig = plt.figure()

x = np.arange(-6, 6, 0.1)

y = np.arange(-6, 6, 0.1)

xx, yy = np.meshgrid(x, y)
z = yy**2 - xx
levels = [-10,-5,0,5,10]
cp = plt.contourf(x,y,z, levels = levels, cmap='RdYlGn')
levels = [-1000000,0,10000000]
CS = plt.contour(x,y,z, levels = levels, colors='k')
plt.clabel(CS, inline=1, fontsize=10)
fig.colorbar(cp)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
