import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi", "Priya", "Deva"],
    "Maths": [67, 86, 89, 97, 67, 56],
    "Python": [90, 76, 97, 76, 98, 97],
    "AI": [89, 90, 79, 98, 98, 78]
}

df = pd.DataFrame(data)
df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1)
print("===== HIGH PERFORMERS =====")
high = df[df["Average"] >= 85]
print(high)
print("\n===== SORTED STUDENTS =====")
sorted_df = df.sort_values("Average", ascending=False)
print(sorted_df)

#Mini Project

import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi", "Priya", "Deva"],
    "Maths": [67, 86, 89, 97, 67, 56],
    "Python": [90, 76, 97, 76, 98, 97],
    "AI": [89, 90, 79, 98, 98, 78]
}

df=pd.DataFrame(data)
df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1)
print("===== STUDENT PERFORMANCE ANALYSIS =====")
print("All Students")
print(df)
print("High Performers:")
high = df[df["Average"] >= 85]
print(high)
print("Python Top Students:")
python=df[df["Python"] >=90]
print("Maths + AI Strong Students:")
others=df[(df["Maths"] >=80) & (df["AI"]>=80)]
print(others)
print("===== RANKING =====")
ranking = df.sort_values("Average", ascending=False).reset_index(drop=True)
ranking["Rank"] = ranking.index + 1
print(ranking)