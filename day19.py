#AI Student Scoring System

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
dot=np.dot(marks, weights)
high=np.argmax(dot)
std_high=names[high]
mark_high=dot[high]
low=np.argmin(dot)
std_low=names[low]
mark_low=dot[low]
overall_avg=np.mean(avg)
print("===== WEIGHTED STUDENT SCORE =====")
for i in range(len(names)):
    print(f"{names[i]} :{np.dot(marks[i], weights):.2f}") 

print(f"Best Student   :{std_high}")
print(f"Best Score     :{mark_high}")
print(f"Lowest Student :{std_low}")
print(f"Lowest Score   :{mark_low}")
print(f"Overall Average:{overall_avg:.2f}")