import seaborn as sns
import matplotlib.pyplot as plt

marks = [45, 52, 55, 60, 62, 65, 68, 70, 72, 75, 78, 95]

sns.boxplot(y=marks)

plt.title("Distribution of Student Marks")
plt.ylabel("Marks")

plt.show()

#short Practice
ages = [18, 19, 20, 20, 21, 21, 22, 22, 23, 24, 45]
sns.boxplot(y=ages)
plt.title("Distribution of Student Ages")
plt.ylabel("Ages")
plt.show()

#Small Project Task: Student Performance EDA

marks = [45, 52, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95, 98, 45]
sns.boxplot(y=marks)    
plt.title("Student Performance EDA")
plt.ylabel("Marks")
plt.show()