import numpy as np
import matplotlib.pyplot as plt

from scipy.special import binom
from fractions import Fraction

x = np.array([binom(14, n) for n in range(4, 10+1)])
x = x / sum(x)
print(x)

plt.plot(np.arange(len(x))+4, x)
plt.show()