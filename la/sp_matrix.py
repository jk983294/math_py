import numpy as np
import scipy as sp
from scipy import linalg

A = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
linalg.inv(A)
linalg.pinv(A)  # generalized inverse
A.dot(linalg.inv(A))
linalg.det(A)
linalg.norm(A)
linalg.norm(A, "fro")  # frobenius norm
linalg.norm(A, 1)  # L1 norm (max column sum)
linalg.norm(A, -1)
linalg.norm(A, np.inf)  # L inf norm (max row sum)

# eigen
A = np.array([[1, 2], [3, 4]])
la, v = linalg.eig(A)
l1, l2 = la
print(l1, l2)   # eigenvalues
print(v[:, 0])   # first eigenvector
print(v[:, 1])   # second eigenvector
print(np.sum(abs(v**2), axis=0))  # eigenvectors are unitary
