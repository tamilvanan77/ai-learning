import numpy as np

hours = [1, 2, 3, 4, 5]
marks = [40, 50, 60, 70, 80]

correlation = np.corrcoef(hours, marks)

print(correlation)

#Practice

hours = [1, 2, 3, 4, 5, 6, 7]
marks = [35, 42, 50, 58, 65, 73, 80]

correlation = np.corrcoef(hours,marks)
print(correlation)


#vectors

A = np.array([10, 20, 30])
B = np.array([5, 15, 25])

print(A+B)
print(A-B)
print(A*3)


#Dot product