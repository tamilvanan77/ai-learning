import pandas as pd

df = pd.read_csv("./csv files/students.csv")

print(df.head(1))
print(df.tail(1))
print(df.shape)
print(df.columns)



#Example Coding

import pandas as pd

df = pd.read_csv("./csv files/student.csv")

print("First 5 Students:")
print(df.head())

print("Dataset Shape:")
print(df.shape)

print("Column Names:")
print(df.columns)

df.to_csv("students_output.csv",index=False)

#Mini Project — Student CSV Analyzer
import pandas as pd
df=pd.read_csv("./csv files/student.csv")
print(df)
df["Average"]=df[["Maths","Python","AI"]].mean(axis=1).round(2)
def Performance(avg):
    if avg>=90:
        return "Excellent"
    elif avg>=70:
        return "Good"
    else:
        return"Need improve"

df["Performance"]=df["Average"].apply(Performance)
print(df)
high=df[df["Average"]>=85]
print("High Performers:")
print(high)
df.to_csv("student_output1.csv",index=False)