import numpy as np

students = ["Arun", "Bala", "Kumar", "Ravi", "Siva", "Vijay",
            "Ajay", "Karthik", "Mani", "Rahul"]

age = [20, 21, 20, 22, 21, 20, 22, 21, 20, 22]

maths = [78, 85, 62, 90, 72, 88, 95, 68, 81, 76]

python = [85, 92, 70, 95, 80, 90, 98, 75, 87, 79]

ai = [82, 88, 68, 91, 75, 94, 96, 72, 85, 80]

sql = [75, 80, 65, 89, 78, 85, 92, 70, 83, 77]

#total number of student
total_std=len(students)
print(f"Total Students :{total_std}")
highest_mark=np.max(python)
print(f"Highest Python mark :{highest_mark}")
lowest_mark=np.min(python)
print(f"Lowest Python mark :{lowest_mark}")
avg_mark=np.mean(python)
print(f"Average Python mark :{avg_mark}")

def python_above(python):
    above=[]
    for mark in python:
        if 80<=mark:
            above.append(mark)

    return above

max= python_above(python)
print(f"scored 80 or above in Python:{max}")

def python_bellow(python):
    bellow=[]
    for mark in python:
        if 50>=mark:
            bellow.append(mark)

    return bellow

min=python_bellow(python)
print(f"scored below 50 in Python:{min}")


#numpy

#mean

cal_mean_py=np.mean(python)
print(f"Python Mean{cal_mean_py}")
cal_mean_ma=np.mean(maths)
print(f"Maths Mean{cal_mean_ma}")
cal_mean_ai=np.mean(ai)
print(f"AI Mean{cal_mean_ai}")
cal_mean_sql=np.mean(sql)
print(f"SQL Mean{cal_mean_sql}")

#Maximum

cal_max_py=np.max(python)
print(f"Python Maximum :{cal_max_py}")
cal_max_ma=np.max(maths)
print(f"Maths Maximum :{cal_max_ma}")
cal_max_ai=np.max(ai)
print(f"AI Maximum :{cal_max_ai}")
cal_max_sql=np.max(sql)
print(f"SQL Maximum :{cal_max_sql}")

#Minimum

cal_min_py=np.min(python)
print(f"Python Minimum :{cal_min_py}")
cal_min_ma=np.min(maths)
print(f"Maths Minimum :{cal_min_ma}")
cal_min_ai=np.min(ai)
print(f"AI Minimum :{cal_min_ai}")
cal_min_sql=np.min(sql)
print(f"SQL Minimum :{cal_min_sql}")

#Total

cal_sum_py=np.sum(python)
print(f"Python Total :{cal_sum_py}")
cal_sum_ma=np.sum(maths)
print(f"Maths  Total :{cal_sum_ma}")
cal_sum_ai=np.sum(ai)
print(f"AI  Total :{cal_sum_ai}")
cal_sum_sql=np.sum(sql)
print(f"SQL  Total:{cal_sum_sql}")


cal_std_py=np.std(python)
print(f"Python Standard deviation:{cal_std_py:.2f}")
cal_std_ma=np.std(maths)
print(f"Maths Standard deviation:{cal_std_ma:.2f}")
cal_std_ai=np.std(ai)
print(f"AI Standard deviation:{cal_std_ai:.2f}")
cal_std_sql=np.std(sql)
print(f"SQL Standard deviation:{cal_std_sql:.2f}")


#Pandas
import pandas as pd

df=pd.DataFrame({
    "Student":students,
    "Age":age,
    "Maths":maths,
    "AI":ai,
    "SQL":sql
})
print(df)
first=df.head()
print(f"first 5 students :{first}")
last=df.tail()
print(f"last 5 students{last}")
df["Avarage"]=df[["Maths","AI","SQL"]].mean(axis=1).round(2)
print(df)

highest=df["Avarage"].max()
print(highest)
lowest=df["Avarage"].min()
print(lowest)

#Matplotlib

import matplotlib.pyplot as plt

plt.bar(students,python)
plt.title("Python marks of all students")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()


plt.plot(students,python)
plt.title("Python marks of all students")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

plt.hist(students,bins=5)
plt.title("Distribution of Python marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

plt.scatter(python,ai)
plt.title("Relationship between Python and AI marks.")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

#Seaborn

import seaborn as sns
df_heat=pd.DataFrame({
    "Maths":maths,
    "Python":python,
    "AI":ai,
    "SQl":sql,
},index=students)

sns.heatmap(df_heat,annot=True)
plt.show()
def hight_mark(python):
    high = 0
    for mark in python:
        if mark>=high:
            high=mark
    return high

h=hight_mark(python)
print(h)