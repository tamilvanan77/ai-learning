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
        if student["marks"]>=80:
            high.append(student)
    return high
def get_average_performers(students):
    avg=[]
    for student in students:
        if 60<=student["marks"]<=79:
            avg.append(student)
    return avg
def get_needs_improvement(students):
    need=[]
    for student in students:
        if student["marks"]<60:
            need.append(student)
    return need

students = [
    {"name": "Arun", "marks": 85},
    {"name": "Bala", "marks": 32},
    {"name": "Kavi", "marks": 67},
    {"name": "Ravi", "marks": 91},
    {"name": "Priya", "marks": 76},
    {"name": "Deva", "marks": 100}
]

high=get_high_performers(students)
avg=get_average_performers(students)
need=get_needs_improvement(students)
print("High Performers")
for student in high:
    print(student["name"],"-",student["marks"])
print("Average Performers")
for student in avg:
    print(student["name"],"-",student["marks"])
print("Needs Improvement")
for student in need:
    print(student["name"],"-",student["marks"])

