#Matplotlib & Seaborn — Zero to Hero
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)

plt.title("My First Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

#Bar Chart

students = ["Arun", "Bala", "Kavi", "Ravi"]
marks = [80, 65, 90, 75]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

# bar chart

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 220]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# Histogram

marks = [45, 50, 52, 60, 65, 67, 70, 72, 75, 78, 80, 85, 90, 92, 95]

plt.hist(marks, bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

#scatter plot

hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [40, 45, 50, 58, 65, 72, 80, 88]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()