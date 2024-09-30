import numpy as np

np.arange(6).reshape(2, 3)
np.arange(6).reshape(3, 2)


A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[5, 6], [7, 8]])
y = np.matrix([[1],[2]])
result_add = A + B
result_sub = A - B
result_matmul = A @ B # A * B
result_transpose = A.T
result_inverse = A.I

# multiply
result_dot = np.dot(A, B)
result_matmul = np.matmul(A, B)
A @ y  # matrix * col_vector

# transpose
result_transpose = np.transpose(A)

# inverse
np.linalg.inv(A)  # inversion

np.linalg.det(A)  # determinant
eigenvalues, eigenvectors = np.linalg.eig(A)  # eigen
np.trace(A)
np.diagonal(A)
np.linalg.solve(A, y)