#Lists in Python

#List Index

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)

#Apple   → 0
#Banana  → 1
#Mango   → 2
#Orange  → 3

#Orange → -1
#Mango  → -2
#Banana → -3
#Apple  → -4

print(fruits[0])
print(fruits[2])
print(fruits[-1])

fruits[1] = "Orange"
print(fruits)

fruits.append("Mango")
print(fruits)

fruits.insert(1, "Banana")
print(fruits)

fruits.remove("Banana")
print(fruits)

fruits.pop(1)
print(fruits)

marks = [85, 90, 78, 95, 88]
print(len(marks))

for mark in marks:
    print(mark)

for fruits in fruits:
    print(fruits)

#List + Function

def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)


marks = [85, 90, 78, 95, 88]

average = calculate_average(marks)

print(f"Average: {average:.2f}")

#List + Function for Average

def calculate_average(marks):
    total = sum(marks)
    count = len(marks)

    return total / count


marks = [80, 90, 70, 85, 95]

average = calculate_average(marks)

print("Average:", average)

#List + Function + if

def count_passed(marks):
    count = 0

    for mark in marks:
        if mark >= 35:
            count += 1

    return count


marks = [80, 20, 55, 30, 90]

passed = count_passed(marks)

print("Students Passed:", passed)

#List + Function + return
def find_even(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


numbers = [10, 15, 22, 31, 40, 55, 60]

result = find_even(numbers)

print(result)

# Practice
#find even number

def find_even(numbers):
    even_number=[]
    for numbers in numbers:
        if (numbers%2)==0:
            even_number.append(numbers)
    return even_number

numbers = [12, 25, 18, 40, 33, 50]

even=find_even(numbers)
print(even)

#find odd number
def find_odd(numbers):
    even_number=[]
    for numbers in numbers:
        if numbers%2 != 0:
            even_number.append(numbers)
    return even_number

numbers = [12, 25, 18, 40, 33, 50]
result=find_odd(numbers)
print(result)

#pass filtering

def filter_passed(marks):
    total=[]
    for marks in marks:
        if marks >= 35 :
            total.append(marks)
    return total
            

marks = [80, 25, 67, 34, 90, 45]

result=filter_passed(marks)
print(f"passed:{result}")
