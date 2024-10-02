import numpy as np
import scipy as sp
from scipy import linalg

A = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])
x = np.linalg.solve(A, b)

# least square
c1, c2 = 5.0, 2.0
i = np.r_[1:11]
xi = 0.1 * i
yi = c1 * np.exp(-xi) + c2 * xi
yi = yi + np.random.randn(len(yi)) * 0.01  # add noise
A = np.c_[np.exp(-xi)[:, np.newaxis], xi[:, np.newaxis]]
c, resid, rank, sigma = linalg.lstsq(A, yi)
