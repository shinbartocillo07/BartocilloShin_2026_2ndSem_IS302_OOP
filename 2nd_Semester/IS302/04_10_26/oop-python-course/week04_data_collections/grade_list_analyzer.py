grades_SGB = []
for i in range(1, 6):
    grade = float(input(f"Enter grade {i}: "))
    grades_SGB.append(grade)

average = sum(grades_SGB) / len(grades_SGB)
highest = max(grades_SGB)
lowest = min(grades_SGB)

print(f"Average Grade: {average:.1f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")
