import numpy as np

x = np.array([1,2,3], dtype=np.float32)
y = np.array([1,2,3], dtype=np.float32)
z = np.matrix([[1],[0],[0]]) # column vector
z1 = np.matrix([[1, 0, 0]]) # row vector
x.shape

x + y
x - y
x * y
x / y
np.sum(x)
np.dot(x, y) # inner product
np.transpose(x.reshape((1, -1))) # first convert to row vector, then transpose

np.arange(start=1, stop=5, step=1)  # [1, 2, 3, 4]
np.linspace(start=1, stop=5, num=3) # [1., 3., 5.]
np.zeros(3)                         # [1, 1, 1]
np.empty(3)                         # [0., 0., 0.]
np.ones(3)                          # [0., 0., 0.]
np.full(3, 2)                       # [2, 2, 2]

# reduce
np.min(x)
np.max(x)
np.sum(x)
np.prod(x)

np.sin(x)
np.cos(x)
np.tan(x)
np.exp(x)
np.log(x)