#Pandas Data Cleaning & Missing Values
import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi", "Priya"],
    "Maths": [67, 86, 89, None, 67],
    "Python": [90, None, 97, 76, 98],
    "AI": [89, 90, None, 98, 98]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing marks with the subject average
df["Maths"] = df["Maths"].fillna(df["Maths"].mean())
df["Python"] = df["Python"].fillna(df["Python"].mean())
df["AI"] = df["AI"].fillna(df["AI"].mean())

print("\nCleaned Data:")
print(df)

#Short Practice

df = pd.DataFrame({
    "Name": ["Arun", "Bala", "Kavi"],
    "Marks": [80, None, 90]
})

df=pd.DataFrame(df)
print(df.isnull().sum())
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())

print(df)

#Mini Project — Clean Student Dataset

import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi", "Priya"],
    "Maths": [67, 86, 89, None, 67],
    "Python": [90, None, 97, 76, 98],
    "AI": [89, 90, None, 98, 98]
}

df=pd.DataFrame(data)
print(df)
print("Missing Values:")
print(df.isnull().sum())
df["Maths"]=df["Maths"].fillna(df["Maths"].mean())
df["Python"]=df["Python"].fillna(df["Python"].mean())
df["AI"]=df["AI"].fillna(df["AI"].mean())
print("Handling Missing values:")
print(df)
df["Average"]=df[["AI","Maths","Python"]].mean(axis=1).round(2)
print("Average Marks:")
print(df)
ranking = df.sort_values("Average",ascending=False).reset_index(drop=True)
ranking["Rank"] = ranking.index + 1
print(ranking)
best = ranking.iloc[0]
print("Best Student:", best["Name"])
print("Best Average:", best["Average"])