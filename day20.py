import numpy as np

marks = np.array([40, 50, 60, 70, 80, 90, 100])

minimum = np.min(marks)
maximum = np.max(marks)

normalized = (marks - minimum) / (maximum - minimum)

print(normalized)

#AI Uses Normalization
#Short Practice

marks = np.array([30, 40, 50, 60, 70, 80, 90])
minimum = np.min(marks)
maximum = np.max(marks)

normalized = (marks - minimum) / (maximum - minimum)

print(normalized)

# Mini Project — Normalize Student Marks

marks = np.array([
    [85, 78, 92],
    [67, 88, 76],
    [95, 91, 89],
    [45, 52, 48],
    [72, 69, 80],
    [88, 84, 90]
])
names = np.array([
    "Arun",
    "Bala",
    "Kavi",
    "Ravi",
    "Priya",
    "Deva"
])

highest = np.max(marks)
lowest = np.min(marks)
normalized = (marks - lowest) / (highest - lowest)
normalized_avg = np.mean(normalized, axis=1)
best = np.argmax(normalized_avg)

print("Original Marks:")
print(marks)

print("\nNormalized Marks:")
print(normalized.round(2))
print(f"best student :{names[best]}")
print(f"best Average :{np.mean(normalized_avg[best]):.2f}")