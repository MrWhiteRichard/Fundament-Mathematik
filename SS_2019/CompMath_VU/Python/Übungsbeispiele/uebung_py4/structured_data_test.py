"""
From the Website:
https://jakevdp.github.io/PythonDataScienceHandbook/02.09-structured-data-numpy.html
"""

import numpy as np

name = np.array(['Alice', 'Bob', 'Cathy', 'Doug'])
age = np.array([25, 45, 37, 19])
weight = np.array([55.0, 85.5, 68.0, 61.5])

data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})
print(data.dtype)

data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)
