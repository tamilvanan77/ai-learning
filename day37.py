#Matplotlib Pie Chart
import matplotlib.pyplot as plt

expenses = [3000, 2000, 1500, 1000]
categories = ["Food", "Travel", "Shopping", "Other"]

plt.pie(expenses, labels=categories,autopct="%1.1f%%")
plt.title("Monthly Expenses")
plt.show()


#Short Practice
subjects = ["Python", "AI", "SQL", "Maths"]
hours = [10, 8, 5, 7]
plt.pie(hours,labels=subjects,autopct="%1.1f%%")
plt.title("Study Hours Distribution")
plt.show()

#Mini Project Data — Student Study Time Analysis

activities = ["Coding", "Reading", "Projects", "Practice", "Break"]
hours = [4, 2, 3, 2, 1]

plt.pie(hours, labels=activities, autopct="%1.1f%%")
plt.title("Student Study Time Analysis")
plt.show()