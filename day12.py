#Practice Exercise

def get_failed_students(students):
    failed=[]
    for student in students:
        if student["marks"]<35:
            failed.append(student)
    return failed

students = [
    {"name": "Arun", "marks": 85},
    {"name": "Bala", "marks": 32},
    {"name": "Kavi", "marks": 67},
    {"name": "Ravi", "marks": 91},
    {"name": "Priya", "marks": 76}
]

result=get_failed_students(students)
print(result)


#Mini Project

def get_high_performers(students):
    high=[]
    for student in students:
        if students["marks"]>=80:
            high.append(student)
    return high

students = [
    {"name": "Arun", "marks": 85},
    {"name": "Bala", "marks": 32},
    {"name": "Kavi", "marks": 67},
    {"name": "Ravi", "marks": 91},
    {"name": "Priya", "marks": 76},
    {"name": "Deva", "marks": 100}
]

high=get_high_performers(students)

for key,value in high:
    print