#numpy
#Your First NumPy Program
import numpy as np
marks = np.array([85, 32, 67, 91, 76])
print(marks)

#NumPy Instead of a Normal List

import numpy as np
marks = np.array([85, 32, 67, 91, 76])
print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))

#Short Practice Exercise

import numpy as np
marks = np.array([78, 85, 92, 67, 45, 88])
print(f"Total   :{np.sum(marks)}")
print(f"Average :{np.mean(marks)}")
print(f"Highest :{np.max(marks)}")
print(f"Lowest   :{np.min(marks)}")

#Mini Project

import numpy as np
marks = np.array([85, 32, 67, 91, 76, 100])
print("===== NUMPY STUDENT ANALYSIS =====")
print(f"Marks   :{marks}")
print(f"Total   :{np.sum(marks)}")
print(f"Average :{np.mean(marks):.2f}")
print(f"Highest :{np.max(marks)}")
print(f"Lowest  :{np.min(marks)}")

print(marks[0])  # 85
print(marks[3])  # 91
print(marks[5])  # 100
#using nagative value
print(marks[0])
print(marks[2])
print(marks[-1])

#Quick practice

import numpy as np

marks = np.array([85, 32, 67, 91, 76, 100])

print("Median:", np.median(marks))
print("Std:", np.std(marks))
print("Highest Index:", np.argmax(marks))
print("Lowest Index:", np.argmin(marks))
print("Sorted:", np.sort(marks))
print("Number of Values:", np.size(marks))
print("Shape:", np.shape(marks))