#Matplotlib — Histogram
import matplotlib.pyplot as plt

marks = [45, 50, 52, 60, 62, 65, 67, 70, 72, 75, 80, 85, 90]

plt.hist(marks)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

#Short Practice

marks = [45, 52, 58, 61, 65, 67, 70, 72, 75, 78, 80, 84, 88, 91, 95]
plt.hist(marks,bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks") 
plt.ylabel("Number of Students")
plt.show()

#Mine project

marks = [
    45, 52, 58, 61, 64,
    67, 69, 70, 72, 74,
    76, 78, 80, 82, 84,
    86, 88, 90, 92, 95
]
total_bin=len(marks)
plt.hist(marks,bins=10)
plt.title("Marks Distribution")
plt.xlabel("Marks") 
plt.ylabel("Number of Students")
plt.show()