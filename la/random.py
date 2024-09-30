import numpy as np

# vector
np.random.rand(3)                           # uniform [0, 1]
np.random.randn(3)                          # standard gaussian
np.random.randint(0, 10, size=3)            # discrete uniform
np.random.normal(loc=0, scale=10, size=3)   # gaussian

# matrix
np.random.rand(3, 2)  # uniform
np.random.randn(3, 2)  # gaussian
np.random.randint(0, 10, size=(2, 3))  # discrete uniform
np.random.normal(loc=0, scale=10, size=(2, 3)) # normal