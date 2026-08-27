#pandas concept
import pandas as pd
data = {
    "Name": ["Arun", "Bala", "Kavi", "Ravi"],
    "Math": [85, 67, 95, 45],
    "Python": [78, 88, 91, 52],
    "AI": [92, 76, 89, 48]
}
df = pd.DataFrame(data)
print(df)
print(df["Math"])
print(df["Math"].mean())

#Short Practice
python_avg = df["Python"].mean()
ai_highest = df["AI"].max()

print("Python Average:", python_avg)
print("Highest AI Mark:", ai_highest)