import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

students = ["Arun", "Bala", "Kumar", "Ravi", "Siva", "Vijay"]
maths = [78, 85, 62, 90, 72, 88]
python = [85, 92, 70, 95, 80, 90]
ai = [82, 88, 68, 91, 75, 94]
sql = [75, 80, 65, 89, 78, 85]

#create dataframe
df=pd.DataFrame({
    "Student": students,
    "Maths": maths,
    "Python": python,
    "AI": ai,
    "SQL": sql
})
print(df)


#bar chart
plt.bar(students,python)
plt.title("Student Marks in python")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()
#line chart
plt.plot(students,python)
plt.title("Student Marks in python")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()
#histogram
plt.hist(python,bins=5)
plt.title("Python")
plt.xlabel("Marks")
plt.show()

#scatter plot

plt.scatter(python,ai)
plt.title("Relation between python and AI")
plt.xlabel("Python")
plt.ylabel("AI")
plt.show()

#heatmap
df_heatmap=pd.DataFrame({
    "Maths": maths,
    "Python": python,
    "AI": ai,
    "SQL": sql
},index=students)
print(df_heatmap)
sns.heatmap(df_heatmap, annot=True)
plt.title("Student Performance Heatmap")
plt.show()