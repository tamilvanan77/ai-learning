#Mini Project — Student Data Analysis
import pandas as pd
data={
    "Name":["Arun","Bala","Kavi","Ravi","Priya","Deva"],
    "Maths":[67,86,89,97,67,56],
    "Python":[90,76,97,76,98,97],
    "AI":[89,90,79,98,98,78]
    }
df=pd.DataFrame(data)

df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1)
best = df["Average"].idxmax()

print(df)
print("Best Student:", df.loc[best, "Name"])
print("Best Average:", df.loc[best, "Average"])