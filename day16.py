import numpy as np
#A 1D array is like one row
marks = np.array([85, 32, 67, 91])
#A 2D array is like a table
students = np.array([
    [85, 32, 67],
    [91, 76, 100],
    [45, 58, 82]
])

print("Shape:", students.shape)
print(students[1])
print(students[:, 0]) #get entire column


#Calculate by row or column
cal=np.mean(students)
print(f"{cal:.2f}")
print(np.mean(students, axis=0))

#Short Practice
marks = np.array([
    [80, 75, 90],
    [65, 70, 85],
    [95, 88, 92]
])

print(np.shape(marks))
print(marks[0])
print(marks[:,2])
print(np.mean(marks , axis=1))

#Small Project — Student Performance Analyzer
import numpy as np

marks = np.array([
    [85, 78, 92],
    [67, 88, 76],
    [95, 91, 89],
    [45, 52, 48],
    [72, 69, 80],
    [88, 84, 90]
])

total = np.shape(marks)

student = total[0]
subject = total[1]

high = np.max(marks)
low = np.min(marks)

student_avg = np.mean(marks, axis=1)
subject_avg = np.mean(marks, axis=0)

# High Performers
high_performers = student_avg[student_avg >= 80]

# Pass and Fail
passed = student_avg[student_avg >= 50]
failed = student_avg[student_avg < 50]

pass_count = len(passed)
fail_count = len(failed)

pass_percentage = (pass_count / student) * 100


print("===== STUDENT PERFORMANCE ANALYZER =====")

print(f"Total Students     : {student}")
print(f"Total Subjects     : {subject}")

print(f"Student Averages   : {student_avg.round(2)}")
print(f"Subject Averages   : {subject_avg.round(2)}")

print(f"Highest Mark       : {high}")
print(f"Lowest Mark        : {low}")

print(f"High Performers    : {high_performers.round(2)}")
print(f"Pass Count         : {pass_count}")
print(f"Fail Count         : {fail_count}")
print(f"Pass Percentage    : {pass_percentage:.2f}%")