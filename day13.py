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

def performance_summary(students,high,avg,need):
    summary = {
    "total": len(students),
    "high": len(high),
    "average": len(avg),
    "needs_improvement": len(need)
}
    return summary

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
summary=performance_summary(students,high,avg,need)
print("High Performers")
for student in high:
    print(student["name"],"-",student["marks"])
print("Average Performers")
for student in avg:
    print(student["name"],"-",student["marks"])
print("Needs Improvement")
for student in need:
    print(student["name"],"-",student["marks"])
print("Student Summary")
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

def performance_summary(students,high,avg,need):
    summary = {
    "total": len(students),
    "high": len(high),
    "average": len(avg),
    "needs_improvement": len(need)
}
    return summary

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
summary=performance_summary(students,high,avg,need)
print("High Performers")
for student in high:
    print(student["name"],"-",student["marks"])
print("Average Performers")
for student in avg:
    print(student["name"],"-",student["marks"])
print("Needs Improvement")
for student in need:
    print(student["name"],"-",student["marks"])
print("Student Summary")
for key, value in summary.items():
    print(key, ":", value)