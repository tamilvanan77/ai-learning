#List of Dictionaries + Data Analysis
students = [
    {"name": "Arun", "marks": 85},
    {"name": "Bala", "marks": 32},
    {"name": "Kavi", "marks": 67},
    {"name": "Ravi", "marks": 91}
]

passed = 0

for student in students:
    if student["marks"] >= 35:
        passed += 1

print("Passed Students:", passed)

#Put the Logic Inside a Function

def count_passed(students):
    passed = 0

    for student in students:
        if student["marks"] >= 35:
            passed += 1

    return passed


students = [
    {"name": "Arun", "marks": 85},
    {"name": "Bala", "marks": 32},
    {"name": "Kavi", "marks": 67},
    {"name": "Ravi", "marks": 91}
]

result = count_passed(students)

print("Passed:", result)

#Short Practice Exercise

def count_failed(students):
    failed=0
    for student in students:
        if student["marks"]<35:
            failed+=1
    return failed


students = [
    {"name": "Arun", "marks": 85},
    {"name": "Bala", "marks": 32},
    {"name": "Kavi", "marks": 67},
    {"name": "Ravi", "marks": 91}
]

count=count_failed(students)

print(f"Failed:{count}")

# Mini Project

def count_passed(students):
    passed=0
    for student in students:
        if student["marks"]>=35:
            passed+=1
    return passed

def count_failed(students):
    failed=0
    for student in students:
        if student["marks"]<35:
            failed+=1
    return failed
def calculate_average(students):
    cal=0
    for student in students:
        cal+=student["marks"]
    return cal/len(students)

def find_highest(students):
    highest = students[0]["marks"]

    for student in students:
        if student["marks"] > highest:
            highest = student["marks"]

    return highest
def find_lowest(students):
    lowest = students[0]["marks"]

    for student in students:
        if student["marks"] < lowest:
            lowest = student["marks"]

    return lowest

students = [
    {"name": "Arun", "marks": 85},
    {"name": "Bala", "marks": 32},
    {"name": "Kavi", "marks": 67},
    {"name": "Ravi", "marks": 91},
    {"name": "Priya", "marks": 76}
]

total=(len(students))
failed=count_failed(students)
passed=count_passed(students)
average=calculate_average(students)
highest=find_highest(students)
lowest=find_lowest(students)

print("===== STUDENT ANALYSIS =====")
print(f"Total Students   :{total}")
print(f"passed           :{passed}")
print(f"Failed           :{failed}")
print(f"Average Marks    :{average}")
print(f"Highest Marks    :{highest}")
print(f"Lowest Marks     :{lowest}")