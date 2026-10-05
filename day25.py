#Pandas groupby() for AI Data Analysis

import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi", "Priya", "Deva"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "Maths": [67, 86, 89, 97, 67, 56],
    "Python": [90, 76, 97, 76, 98, 97],
    "AI": [89, 90, 79, 98, 98, 78]
}

df = pd.DataFrame(data)

# Average AI mark for each department
department_ai = df.groupby("Department")["AI"].mean()

print(department_ai)
print(df)
result = df.groupby("Department")[["Maths", "Python", "AI"]].mean().round(2)

print(result)

#Short Practice

Python=df.groupby("Department")["Python"].mean()
ai=df.groupby("Department")["AI"].mean()
print(Python)
print(ai)

#Department Performance Analyzer
import pandas as pd
data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi", "Priya", "Deva"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "Maths": [67, 86, 89, 97, 67, 56],
    "Python": [90, 76, 97, 76, 98, 97],
    "AI": [89, 90, 79, 98, 98, 78]
}

df=pd.DataFrame(data)
df["Average"]=df[["Maths","Python","AI"]].mean(axis=1).round(2)
avg=df.groupby("Department")["Average"].mean()
print(avg)
best = df.loc[df.groupby("Department")["Average"].idxmax()]
print(best)
ranking = (
    df.groupby("Department")["Average"]
      .mean()
      .sort_values(ascending=False)
)

print(ranking)