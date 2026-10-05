#Matplotlib Scatter Plot

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 55, 65, 75, 85]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()

#Short Practice
hours = [2, 3, 4, 5, 6, 7, 8]
marks = [50, 55, 60, 65, 72, 80, 88]
plt.scatter(hours,marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

#mine project

#Short Practice
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks = [35, 42, 48, 55, 61, 68, 74, 81, 89, 95]
plt.scatter(hours,marks)
plt.title("Student Study Analysis")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()