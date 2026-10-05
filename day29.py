#Pandas + Excel Files

import pandas as pd

df = pd.read_excel("./Excel files/students.xlsx")

print("===== STUDENT DATA =====")
print(df)

df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1).round(2)

print("\n===== STUDENT AVERAGE =====")
print(df)

df.to_excel("student_analysis.xlsx", index=False)

print("\nExcel file saved successfully!")


#Practice


print(df.head(3))
print(df.shape)
print(df.columns)
py_avg=df["Python"].mean()
print(f"Python Average: {py_avg}")

# Mini Project — Excel Student Analyzer

import pandas as pd

df = pd.read_excel("./Excel files/students.xlsx")

# Calculate Average
df["Average"] = df[["Maths", "Python", "AI"]].mean(axis=1).round(2)


# Performance
def Performance(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    else:
        return "Need improve"


df["Performance"] = df["Average"].apply(Performance)


# Sort by Average
df.sort_values("Average", ascending=False, inplace=True)


# Reset index
df.reset_index(drop=True, inplace=True)


# Create Rank
df["Rank"] = df.index + 1


# Find Best Student
best = df.iloc[0]

print("===== STUDENT ANALYSIS =====")
print(df)

print("\nBest Student:", best["Name"])
print("Best Average:", best["Average"])


# Save to Excel
df.to_excel("student_analysis.xlsx", index=False)

print("\nExcel file saved successfully!")