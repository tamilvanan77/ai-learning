#Real Dataset Analysis with Pandas

import pandas as pd

df = pd.read_csv("./csv files/student.csv")

df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1).round(2)

department_average = df.groupby("Department")["Average"].mean().round(2)

print("Average by Department:")
print(department_average)

#Short practice

import pandas as pd
df = pd.read_csv("./csv files/student.csv")
df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1).round(2)
dep_avg = df.groupby("Department")["Average"].mean().round(2)
dep_rank = dep_avg.sort_values(ascending=False)
print("Average by Department:")
print(dep_avg)

rank=df.sort_values("Average",ascending=False).reset_index(drop=True)
print(rank)

hig = rank.iloc[0]

print("Highest Student:")
print(hig)

dep_rank = dep_avg.sort_values(ascending=False)

print(dep_rank)

best_department = dep_rank.index[0]

print("Best Department:", best_department)

#30 Mini Project — Department Performance Analyzer

import pandas as pd
df=pd.read_excel("./Excel files/students.xlsx")
print(df)
df["Average"]=df[["Maths","Python","AI"]].mean(axis=1).round(2)
print(df)

def performance (avg):
    if avg>=90:
        return"Excellent"
    elif avg>=70:
        return"Good"
    else:
        return"Need Improve"

df["Perfomance"]=df["Average"].apply(performance)
print(df)

dep_avg=df.groupby("Department")["Average"].mean().round(2)
print(dep_avg)

dep_ranking=dep_avg.sort_values(ascending=False)
print(f"Department Ranking:{dep_ranking.index[0]}")

df.to_excel("department_analysis.xlsx", index=False)

#Mini Project — Student Data Cleaner

import pandas as pd

df=pd.read_excel("./Excel files/student.xlsx")
print(df)
df.drop_duplicates(inplace=True)
print("Missing Values")
print(df.isnull().sum())
print("Handling missing Values")
df["Python"]=df["Python"].fillna(df["Python"].mean())
df["Maths"]=df["Maths"].fillna(df["Maths"].mean())
df["AI"]=df["AI"].fillna(df["AI"].mean())
print(df)
df["Average"]=df[["Python","Maths","AI"]].mean(axis=1).round(2)
print(df)
def perfomance(avg):
    if avg>=90:
        return"Excellent"
    elif avg>=70:
        return"Good"
    else:
        return"Need Improve"

df["Performance"]=df["Average"].apply(perfomance)
print(df)
df.to_excel("students_cleaned.xlsx")