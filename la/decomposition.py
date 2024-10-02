import numpy as np
import scipy as sp
from scipy import linalg

# SVD: A = U*Sig*Vh
A = np.array([[1, 2, 3], [4, 5, 6]])
M, N = A.shape
U, s, Vh = linalg.svd(A)
Sig = linalg.diagsvd(s, M, N)
U.dot(Sig.dot(Vh))  # check computation

# LU: A = P*L*U
A = np.array([[1, 2], [3, 7]])
linalg.lu(A)

# Cholesky
A = np.array([[1, 2], [3, 7]])
linalg.cholesky(A)

# QR
linalg.qr(A)
