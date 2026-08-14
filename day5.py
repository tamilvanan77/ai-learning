def add(a, b):
    return a + b
print(add(10, 20))
print(add(50, 30))

# Function to display a welcome message

def welcome():
    print("Welcome to Python!")

welcome()

#Function with Parameters

def greet(name):
    print(f"Hello {name}!")

greet("Tamilvanan")
greet("Arun")

# Multiple Parameters

def student(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student("Tamilvanan", 21)

#Return


def add(a, b):
    return a + b

result = add(10, 20)
print(result)

#Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))

#odd or even

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    else:
        return "Odd"


number = int(input("Enter number: "))

print(check_even_odd(number))



#Functions + Loops

def print_numbers(n):

    for i in range(1, n + 1):
        print(i)


print_numbers(5)


#Today's Practice Exercise

def square(number):
    return number * number

number = int(input("Enter a number: "))
print(f"square:{square(number)}")

def cube(number):
    return number * number * number 
number = int(input("Enter a number: "))
print(f"cube:{cube(number)}")

# Student Mark calculator


def calculate_total(tamil,english,maths,science,ssience):
    return tamil+english+maths+science+ssience
def calculate_average(tamil,english,maths,science,ssience):
    return (tamil+english+maths+science+ssience)/5
def check_result(tamil,english,maths,science,ssience):
    if ((tamil+english+maths+science+ssience)/5)>=35:
        return"Pass"
    else:
        return "Fail"
        
tamil=int(input("Enter the Tamil Mark :"))
english=int(input("Enter the English Mark :"))
maths=int(input("Enter the Maths Mark :"))
science=int(input("Enter the Science Mark :"))
ssience=int(input("Enter the Social Science Mark :"))


print("Total :",calculate_total(tamil,english,maths,science,ssience))
print("Average :",calculate_average(tamil,english,maths,science,ssience))
print("Result :",check_result(tamil,english,maths,science,ssience))

