import pandas as pd
data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi", "Priya", "Deva"],
    "Maths": [67, 86, 89, 97, 67, 56],
    "Python": [90, 76, 97, 76, 98, 97],
    "AI": [89, 90, 79, 98, 98, 78]
}
df = pd.DataFrame(data)


#Short Practice

print(df.loc[3])#Print Ravi's complete row
print(df.loc[4, "Python"])#Print Priya's Python mark
print(df.loc[:, ["Name", "AI"]])

#Mini Project

import pandas as pd
data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi", "Priya", "Deva"],
    "Maths": [67, 86, 89, 97, 67, 56],
    "Python": [90, 76, 97, 76, 98, 97],
    "AI": [89, 90, 79, 98, 98, 78]
}
df = pd.DataFrame(data)
df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1)
print("===== STUDENT REPORT =====")
name=df.loc[2,"Name"]
print(f"Name     :{name}")
maths=df.loc[2,"Maths"]
print(f"Maths    :{maths}")
python=df.loc[2,"Python"]
print(f"Python   :{python}")
ai=df.loc[2,"AI"]
print(f"AI       :{ai}")
avg=df.loc[2,"Average"]
print(f"Average  :{avg:.2f}")
