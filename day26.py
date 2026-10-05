#Pandas apply() + Feature Engineering
import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi", "Priya", "Deva"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "Maths": [67, 86, 89, 97, 67, 56],
    "Python": [90, 76, 97, 76, 98, 97],
    "AI": [89, 90, 79, 98, 98, 78]
}

df = pd.DataFrame(data)

# Calculate student average
df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1).round(2)


# Create performance function
def performance(avg):

    if avg >= 85:
        return "Excellent"

    elif avg >= 70:
        return "Good"

    else:
        return "Needs Improvement"


# Apply function
df["Performance"] = df["Average"].apply(performance)


print("===== STUDENT PERFORMANCE =====")

print(df[[
    "Name",
    "Department",
    "Average",
    "Performance"
]])

#Mini Project
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

def performance(avg):
    if avg>=85:
        return "Excellent"
    elif avg>=70:
        return "Good"
    else:
        return "Needs Improvement"

df["Performance"]=df["Average"].apply(performance)

print(df)

def python_level (python):
    if python>=90:
        return "Excellent"
    elif python>=75:
        return "Good"   
    else:
        return"Beginner"

df["Python_Perform"]=df["Python"].apply(python_level)
print(df)

excellent_count = (df["Performance"] == "Excellent").sum()

print("Excellent Students:", excellent_count)