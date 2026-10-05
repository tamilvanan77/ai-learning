#What is Mean?
#Mean is the average value of a group of numbers.

#Formula
 #mean = Sum of all values / Sum of all values​

marks = [45, 50, 55, 60, 65]
value = len(marks)
sum=0
for mark in marks:
    sum+=mark
print(sum/value)

#Median

#Median is the middle value when numbers are arranged in ascending or descending

marks = [45, 52, 60, 65, 70, 75, 80]

length = len(marks)

if length % 2 != 0:
    median = length // 2
    print("Median:", marks[median])

else:
    median1 = length // 2 - 1
    median2 = length // 2
    median = (marks[median1] + marks[median2]) / 2
    print("Median:", median)

#Standed Devition

marks = [10, 20, 30, 40, 50]

# Step 1: Find mean
mean = sum(marks) / len(marks)

# Step 2: Find squared differences
squared_diff = []

for mark in marks:
    difference = mark - mean
    squared_diff.append(difference ** 2)

# Step 3: Find variance
variance = sum(squared_diff) / len(marks)

# Step 4: Find standard deviation
std = variance ** 0.5

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std)
