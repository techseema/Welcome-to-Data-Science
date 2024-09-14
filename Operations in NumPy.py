import numpy as np

# Create two matrices
matrix_A = np.array([[1, 2, 3], [4, 5, 6]])
matrix_B = np.array([[7, 8], [9, 10], [11, 12]])

# Perform matrix multiplication
result = np.dot(matrix_A, matrix_B)

print("Matrix A:")
print(matrix_A)

print("Matrix B:")
print(matrix_B)

print("Result of Matrix Multiplication:")
print(result)