#practice exercise

import numpy as np
marks = np.array([45, 72, 88, 31, 95, 64, 50, 81])
high=marks[marks>=80]
below=marks[marks<50]
pass_count=marks[marks>=50]
print(f"High        :{high}")
print(f"Below       :{below}")
print(f"Pass Count  :{len(pass_count)}")

#or
print(f"Pass Count  :{np.size(pass_count)}")

#Small Project — NumPy Student Analyzer 2.0

import numpy as np
marks = np.array([85, 32, 67, 91, 76, 100, 45, 58, 82, 73])
total=len(marks)
avg= marks[(marks >= 60) & (marks < 80)]
high_perform=marks[marks>80]
passed=marks[(marks >= 50) & (marks < 60)]
fail=marks[marks<50]
low=np.min(marks)
highest=np.max(marks)
pass_count=len(marks[marks>=50])
fail_count=len(marks[marks<50])
pass_per=(pass_count/total)*100

print("===== STUDENT PERFORMANCE ANALYSIS =====")

print(f"Total Students  : {total}")
print(f"Average Marks   : {avg}")
print(f"Highest Marks   : {highest}")
print(f"Lowest Marks    : {low}")

print(f"Passed Marks    : {passed}")
print(f"Failed Marks    : {fail}")

print(f"High Performers : {high_perform}")
print(f"Pass Count      : {pass_count}")
print(f"Fail Count      : {fail_count}")

print(f"Pass Percentage : {pass_per}")