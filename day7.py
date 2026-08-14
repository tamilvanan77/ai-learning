#Accessing Values
student = {
    "name": "Tamil",
    "age": 21,
    "marks": 85
}

print(student["name"])
print(student["marks"])

#Dictionary + Function

def check_student(student):
    if student["marks"] >= 35:
        return "Pass"
    else:
        return "Fail"


student = {
    "name": "Tamil",
    "marks": 85
}

result = check_student(student)

print(f"{student['name']}: {result}")



#Practice

def get_grade(student):
    if student['marks']>=90:
        return "A"
    elif student['marks']>=75:
        return "B"
    elif student['marks']>=60:
        return "C"
    elif student['marks']>=35:
        return "D"
    else:
        return "F"

student = {
    "name": "Arun",
    "marks": 32
}

result=get_grade(student)
print(f"{student['name']} grade is {result}")

#Student Analyzer


def analyze_students(students):
    if students['marks']>=35:
        return "pass"
    else:
        return"Fail"

students = [
    {"name": "Arun", "marks": 85},
    {"name": "Bala", "marks": 32},
    {"name": "Kavi", "marks": 67},
    {"name": "Ravi", "marks": 91}
]
for students in students:
    result=analyze_students(students)
    print(f"{students["name"]} is {result}")

# Practice Exercise

student = {
    "name": "Tamil",
    "marks": 85
}

student["departement"]="AI&DS"
student["marks"]=90
for key,value in student.items():
    print(key,":",value)