name = input("Enter Name : ")
age = int(input("Enter Age : "))
cgpa = float(input("Enter CGPA : "))
department = input("Enter Department : ")

print("----- STUDENT DETAILS -----")
print("Name       :", name)
print("Age        :", age)
print("CGPA       :", cgpa)
print("Department :", department)


#AI Mini Project – BMI Calculator

weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

#Homework

#calculator

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Additional value : {a+b}")
print(f"Subtraction value : {a-b}")
print(f"Division value : {a/b}")
print(f"Multiplication value : {a*b}")

#student profile

name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
dob=str(input("Enter your date of birth: "))
phone=int(input("Enter your phone number: "))
mail=str(input("Enter your email: "))
gender=str(input("Enter your gender: "))
college=str(input("Enter your college name: "))
department=str(input("Enter your department: "))
print("----- STUDENT PROFILE -----")
print("Name          :", name)
print("Age           :", age)
print("Date of Birth :", dob)
print("Phone Number  :", phone)
print("Email         :", mail)
print("Gender        :", gender)
print("College       :", college)
print("Department    :", department)

#Celsius

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")