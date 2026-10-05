#Seaborn Heatmap

import seaborn as sns
import matplotlib.pyplot as plt

data = [
    [80, 70, 90],
    [60, 85, 75],
    [90, 80, 95]
]

sns.heatmap(data, annot=True)

plt.title("Student Marks Heatmap")
plt.show()

#short Practice

data = [
    [80, 75, 90],
    [65, 85, 70],
    [90, 88, 95]
]

sns.heatmap(data, annot=True)

plt.title("Student Marks Heatmap")
plt.show()

#Create a DataFrame

import pandas as pd

data = {
    "Python": [80, 65, 90],
    "AI": [75, 85, 88],
    "SQL": [90, 70, 95]
}

df = pd.DataFrame(data, index=["Student 1", "Student 2", "Student 3"])

sns.heatmap(df, annot=True)

plt.title("Student Marks Heatmap")
plt.show()

#Short Practice

data = {
    "Python": [85, 75, 90],
    "AI": [80, 88, 92],
    "SQL": [70, 82, 95]
}

df=pd.DataFrame(data, index=["Arun", "Bala", "Kumar"])

sns.heatmap(df, annot=True)
plt.title("students in Python, AI, and SQL")
plt.show()