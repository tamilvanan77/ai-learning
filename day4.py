#Mini Project 1 – Multiplication Table
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#Mini Project 2 – Sum of Numbers

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

#Mini Project 3 – Password Attempts

correct_password = "python123"

for attempt in range(3):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")

#Practice Questions
#Program 1
for i in range(1, 100+1):
    print(i)

#Program 2
for i in range(1, 50+1):
    if i % 2 == 0:
        print(i)

#Program 3
for i in range(1, 50+1 ,2):
    print(i)

#Program 4

num=int(input("Enter a number: "))
for i in range(1, num):
    num=num*i
print(f"The Factorial is {num}")

#Program 5
num=int(input("Enter a number: "))
for i in range(num+1):
    print("*"*i)

#Bonus Challenge
star=int(input("Enter a stars: "))
for i in range(star):
    print("*"*(star-i))

#program 1
n=1
while n<=20:
    print(n)
    n+=1
#program 2
n=1
while n<=20:
    if n%2==0:
        print(n)
    n+=1    

#program 3
n=1
while n<=20:
    if n%2!=0:
        print(n)
    n+=1  

#program 4
num=int(input("Enter a number: "))
factorial=1
while num>0:
    factorial=factorial*num
    num-=1
print(f"The Factorial is {factorial}")

#Program 5 (Mini Project)

password="tamil123"
attempt=0
while attempt<3:
    user_password=input("Enter Password: ")
    if user_password==password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")
        attempt+=1

    