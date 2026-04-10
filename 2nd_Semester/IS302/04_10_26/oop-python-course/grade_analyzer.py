student_name = input("Enter student name: ")

grades = []
for i in range(1, 4):
    grade = float(input(f"Enter grade for subject {i}: "))
    grades.append(grade)

average = sum(grades) / len(grades)

if average >= 90:
    remark = "Excellent"
elif average >= 85:
    remark = "Very Good"
elif average >= 80:
    remark = "Good"
elif average >= 75:
    remark = "Fair"
else:
    remark = "Failed"

print(f"\nStudent Name: {student_name}")
print(f"Average Grade: {average:.2f}")
print(f"Remark: {remark}")
