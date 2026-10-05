# line chart

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 220]

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# short practice

tests = ["Test 1", "Test 2", "Test 3", "Test 4", "Test 5"]
marks = [65, 72, 68, 85, 90]

plt.plot(tests,marks, marker="o")
plt.title("Student Test Marks")
plt.xlabel("Test Name")
plt.ylabel("Marks")
plt.show()

#Mini Project — Monthly Sales Analysis
import matplotlib.pyplot as plt

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

sales = [
    120, 150, 135, 180, 200, 175,
    220, 240, 210, 260, 280, 300
]

plt.plot(months,sales,marker="o")
plt.title("Sales analysis in months")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


