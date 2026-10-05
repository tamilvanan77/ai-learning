import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Original Matrix:")
print(A)

print("Transpose:")
print(A.T)
print(np.transpose(A))

#Practice

A = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(A)
B=A.T
print(B)
print(np.shape(A))
print(np.shape(B))