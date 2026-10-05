#Handling Missing Values

import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi"],
    "Maths": [90, None, 85, 75],
    "Python": [88, 76, None, 82]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["Maths"] = df["Maths"].fillna(df["Maths"].mean())
df["Python"] = df["Python"].fillna(df["Python"].mean())

print("\nCleaned Data:")
print(df)

#Short practice

import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi"],
    "Maths": [90, None, 85, 75],
    "Python": [88, 76, None, 82]
}

df=pd.DataFrame(data)
print(df)
print("Missing values")
print(df.isnull().sum())
df["Python"]=df["Python"].fillna(df["Python"].mean())
df["Maths"]=df["Maths"].fillna(df["Maths"].mean())
print(df)


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