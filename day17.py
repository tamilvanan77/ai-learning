#Connect It to Our 2D Dataset
import numpy as np

marks = np.array([
    [85, 78, 92],
    [67, 88, 76],
    [95, 91, 89],
    [45, 52, 48],
    [72, 69, 80],
    [88, 84, 90]
])

student_avg = np.mean(marks, axis=1)
best_index = np.argmax(student_avg)
best_average = student_avg[best_index]

print("Student Averages:", student_avg)
print("Best Student Index:", best_index)
print("Best Student Average:", best_average)

#Give Students Names

names = np.array([
    "Arun",
    "Bala",
    "Kavi",
    "Ravi",
    "Priya",
    "Deva"
])

best_name = names[best_index]

print("Best Student:", best_name)

#Short Practice
import numpy as np

names = np.array(["Arun", "Bala", "Kavi", "Ravi"])
averages = np.array([75.5, 82.3, 91.2, 68.4])
best_index = np.argmax(averages)
std_best=names[best_index]
best_avg=averages[best_index]

print(f"Best Student:{std_best}")
print(f"Best Average:{best_avg}")

#Mini Project

import numpy as np

names = np.array([
    "Arun",
    "Bala",
    "Kavi",
    "Ravi",
    "Priya",
    "Deva"
])

marks = np.array([
    [85, 78, 92],
    [67, 88, 76],
    [95, 91, 89],
    [45, 52, 48],
    [72, 69, 80],
    [88, 84, 90]
])

avg = np.mean(marks, axis=1)

best = np.argmax(avg)

best_student = names[best]
best_average = avg[best]

for i in range(len(names)):
    print(f"{names[i]} : {avg[i]:.2f}")

print(f"Best Student : {best_student}")
print(f"Best Average : {best_average:.2f}")

