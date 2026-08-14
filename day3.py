#Mini Project 1

#Voting Eligibility

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name}, you are eligible to vote.")
else:
    print(f"{name}, you are not eligible to vote.")


#Mini Project 2
#Largest Number

a = int(input("First Number: "))
b = int(input("Second Number: "))

if a > b:
    print(f"{a} is larger")
else:
    print(f"{b} is larger")

#Mini Project 3
#Student Grade

name = input("Student Name: ")
marks = int(input("Marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n------ RESULT ------")
print("Name :", name)
print("Marks:", marks)
print("Grade:", grade)

#AI Mini Project

heart_rate = int(input("Enter Heart Rate: "))

if heart_rate < 60:
    print("Low Heart Rate")

elif heart_rate <= 100:
    print("Normal Heart Rate")

else:
    print("High Heart Rate")


#Practice Questions

#Program 1
num = int(input("Enter a number: "))
if num>=1:
    print(f"{num} is a positive numbeer")
elif num==0:
    print(f"{num} is zero")
else:
    print(f"{num} is a negative number")

#Program 2
age = int(input("Enter Your age: "))
if age<=10:
    print("You are a Child")
elif age<=18:
    print("You are a Teenager")
elif age>=40:
    print("You are an Adult")
else:
    print("You are a Senior Citizen")



#Program 3

leap=int(input("Enter a year: "))
if leap%4==0:
    print(f"{leap} is a leap year")
else:
    print(f"{leap} is not a leap year")

#Program 4
username = input("Enter Username: ")
password = input("Enter Password: ")
udata="admin"
pdata="password"
if username==udata and password==pdata:
    print("Login Successful")
else:
    print("Invalid Username or Password")

#Mentor Challenge

amount = float(input("Enter Amount: "))
withdrawal = float(input("Enter Withdrawal Amount: "))
balance = amount - withdrawal
if balance < 0:
    print("Insufficient Funds")
    print(f"Current Balance: {amount}")
else:
    balance = amount
    print("Transaction Successful")
    print(f"Remaining Balance: {balance}")

#Mentor Challenge

amount = float(input("Enter Amount: "))
print("Select Transaction type:")
print("1. Deposit")
print("2. Withdrawal")
type=int(input("Enter Transaction type (1 or 2): "))
if type==1:
    deposit = float(input("Enter Deposit Amount: "))
    balance = amount + deposit
    amount = balance
    print("Transaction Successful")
    print(f"Current Balance: {amount}")
elif type==2:
    withdrawal = float(input("Enter Withdrawal Amount: "))
    balance = amount - withdrawal
    if amount < withdrawal:
        print("Insufficient Funds")
        print(f"Current Balance: {amount}")
    else:
        amount = balance
        print("Transaction Successful")
        print(f"Remaining Balance: {amount}")
else:
    print("Invalid Transaction Type")
    print("Please select a valid transaction type (1 or 2).")