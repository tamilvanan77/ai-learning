#coding Example
def add_grade(student):
    if student["marks"] >= 90:
        student["grade"] = "A"
    elif student["marks"] >= 75:
        student["grade"] = "B"
    elif student["marks"] >= 60:
        student["grade"] = "C"
    elif student["marks"] >= 35:
        student["grade"] = "D"
    else:
        student["grade"] = "F"


students = [
    {"name": "Arun", "marks": 85},
    {"name": "Bala", "marks": 32},
    {"name": "Kavi", "marks": 67},
    {"name": "Ravi", "marks": 91}
]

for student in students:
    add_grade(student)

for student in students:
    print(student)

#Practice Write a function that adds a "grade" key.
student = {
    "name": "Tamil",
    "marks": 78
}

student["grade"]="B"
print(student)

#Student Analyzer