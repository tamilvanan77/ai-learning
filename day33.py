#Pandas + Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Name": ["Arun", "Bala", "Kavi", "Ravi"],
    "Marks": [80, 65, 90, 75]
})

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")

plt.show()

#seaborn

import seaborn as sns

students = ["Arun", "Bala", "Kavi", "Ravi"]
marks = [80, 65, 90, 75]

sns.barplot(x=students, y=marks)

plt.title("Student Marks")

plt.show()

#scatter plot
sns.scatterplot(
    x="Hours",
    y="Marks",
    data=df
)

plt.show()