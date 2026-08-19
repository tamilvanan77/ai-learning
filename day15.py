import numpy as np

n = int(input("Enter number of students: "))
subjects = 3

names = []
marks = []

for i in range(n):
    name = input(f"\nEnter student {i + 1} name: ")
    names.append(name)

    student_marks = []

    for j in range(subjects):
        mark = float(input(f"Enter mark for Subject {j + 1}: "))
        student_marks.append(mark)

    marks.append(student_marks)

marks_array = np.array(marks)

print("\n===== STUDENT DETAILS =====")

for i in range(n):
    total = np.sum(marks_array[i])
    average = np.mean(marks_array[i])
    
    print(f"\nName    : {names[i]}")
    print(f"Marks   : {marks_array[i]}")
    print(f"Total   : {total}")
    print(f"Average : {average:.2f}")
    print(f"Highest : {np.max(marks_array[i])}")
    print(f"Lowest  : {np.min(marks_array[i])}")

print("\n===== CLASS AVERAGE =====")
print("Class Average:", np.mean(marks_array))