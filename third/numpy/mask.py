import numpy as np
from numpy import ma # import masked arrays

x = np.arange(10)
y = ma.masked_array(x, x<5)
print(y)