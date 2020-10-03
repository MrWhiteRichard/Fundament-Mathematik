import matplotlib.pylab as plt
import numpy as np


p = plt.subplots(2, 2, sharex = True, figsize = (8, 8))
x = np.linspace(-2, 2)

p1 = p[1][0][0]
p2 = p[1][1][0]
p3 = p[1][0][1]
p4 = p[1][1][1]

p1.plot(x, np.sin(4*x), color = 'red') 
p2.plot(x, np.cos(x))
p3.plot(x, np.cos(x) * np.sin(x))
p4.plot(x, np.cos(x) + np.sin(x))

p1.set_xlabel('x')
p2.set_xlabel('x')
p3.set_xlabel('x')
p4.set_xlabel('x')

p1.legend(
    ('sin(4x)', ),
    loc = 'center right',
    fontsize = 'small'
)
p2.legend(
    ('cos(x)', ),
    loc = 'lower center',
    fontsize = 'small'
)
p3.legend(
    ('cos(x)sin(x)', ),
    loc = 'center',
    fontsize = 'small'
)
p4.legend(
    ('cos(x)+sin(x)', ),
    loc = 'lower right',
    fontsize = 'small'
)


plt.show()
