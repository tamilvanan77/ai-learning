#Pandas map() & Categorical Encoding

import pandas as pd

df = pd.DataFrame({
    "Name": ["Arun", "Bala", "Kavi", "Ravi"],
    "Performance": [
        "Excellent",
        "Good",
        "Needs Improvement",
        "Excellent"
    ]
})

df["Score"] = df["Performance"].map({
    "Excellent": 2,
    "Good": 1,
    "Needs Improvement": 0
})

print(df)

#Short Practice

import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi", "Priya", "Deva"],
    "Performance": [
        "Excellent",
        "Good",
        "Average",
        "Poor",
        "Excellent",
        "Good"
    ]
}

df = pd.DataFrame(data)

print(df)
df["Score"]=df["Performance"].map({"Excellent": 3, "Good": 2, "Average": 1, "Poor": 0})
print(df)

#Mini Project — Student ML Encoding System.

import pandas as pd

data = {
    "Name": ["Arun","Bala","Kavi","Ravi","Priya","Deva"],
    "Department": ["CSE","ECE","CSE","ECE","CSE","ECE"],
    "Maths": [67,86,89,97,67,56],
    "Python": [90,76,97,76,98,97],
    "AI": [89,90,79,98,98,78]
}
df = pd.DataFrame(data)
print(df)
df["Average"]=df[["Maths","Python","AI"]].mean(axis=1).round(2)
def Performance (avg):
    if avg>=85:
        return "Excellent"
    elif avg>=70:
        return "Good"
    else:
        return "Needs Improvement"

df["Performance"]=df["Average"].apply(Performance)
print(df)

df["Score"]=df["Performance"].map({"Excellent":2,"Good":1,"Needs Improvement":0})

def python (python):
    if python>=90:
        return "Expert"
    elif python>=70:
        return "Intermediate"
    else:
        return"Beginner"
df["Python_Performance"]=df["Python"].apply(python)
df["Python_Score"]=df["Python_Performance"].map({"Expert":3,"Intermediate":2,"Beginner":1})
print(df)