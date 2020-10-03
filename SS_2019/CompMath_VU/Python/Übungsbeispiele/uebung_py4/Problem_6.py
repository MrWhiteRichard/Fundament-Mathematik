import numpy as np


def script(z):
    N = len(z)

    data = np.zeros(N, dtype = {'names':('real', 'imag', 'norm'),
                                'formats':('float', 'float', 'float')})
    data['real'] = np.real(z)
    data['imag'] = np.imag(z)
    data['norm'] = abs(z) 

    i = np.argsort(data, order = ['norm', 'imag'])
    s = z[i]
    return s[1:-1]


#N = 8
#a = np.random.rand(N)
#b = np.random.rand(N)

p_1 = [3, 4, 5, 12, 8, 15, 7, 24]
p_2 = [4, 3, 12, 5, 15, 8, 24, 7]

a = np.array(p_1[::-1])
b = np.array(p_2[::-1])
z = a + b*1j

print("\n", "Before sorting:", "\n", z)

s = script(z)
print("\n", "After sorting:", "\n", s)
