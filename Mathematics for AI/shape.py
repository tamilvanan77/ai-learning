#shape

import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(a)
print(np.shape(a))




#Print 50
#Print 90
print((a[1][1]))
print((a[2][2]))



#Matrix Operations

A = np.array([
    [2, 4],
    [6, 8]
])

B = np.array([
    [1, 3],
    [5, 7]
])


#Calculate A + B
#Calculate A - B
#Calculate A * B
#Calculate A @ B
print("Addition of A and B")
print(A+B)
print("Subration of A and B")
print(A-B)
print("Multiplicatin of A and B")
print(A*B)
print("Matrix Multiplication of A and B")
print(A@B)

