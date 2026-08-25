#Array Addition
import numpy as np

marks1 = np.array([80, 70, 90])
marks2 = np.array([75, 85, 95])
result = marks1 + marks2
print(result)

#Array Subtraction
result = marks1 - marks2
print(result)

#Multiplication

marks = np.array([10, 20, 30, 40])
result = marks * 2
print(result)

#Division

marks = np.array([80, 60, 90])
result = marks / 10
print(result)

#Array-to-Array Calculation

student1 = np.array([80, 70, 90])
student2 = np.array([60, 75, 85])
total = student1 + student2
print(total)

# dot concepet

marks = np.array([80, 70, 90])
weights = np.array([0.3, 0.3, 0.4])
score = np.dot(marks, weights)
print(score)

#Short Practice
import numpy as np

marks = np.array([80, 70, 90])
bonus = np.array([5, 10, 3])

final_marks = marks + bonus
difference = final_marks - marks
weights = np.array([0.3, 0.3, 0.4])
score = np.dot(marks, weights)
print(final_marks)
print(difference)
print(score)

#mine project

import numpy as np

marks = np.array([
    [85, 78, 92],
    [67, 88, 76],
    [95, 91, 89],
    [45, 52, 48],
    [72, 69, 80],
    [88, 84, 90]
])

weights = np.array([0.3, 0.3, 0.4])

names = np.array([
    "Arun",
    "Bala",
    "Kavi",
    "Ravi",
    "Priya",
    "Deva"
])
avg=np.mean(marks, axis=1)
print("===== WEIGHTED STUDENT SCORE =====")
for i in range(len(names)):
    print(f"{names[i]} :{np.dot(marks[i], weights):.2f}") 