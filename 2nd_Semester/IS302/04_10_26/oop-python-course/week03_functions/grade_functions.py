def calculate_average(grades):
    return sum(grades) / len(grades)


def get_remark(average):
    if average >= 90:
        return "Excellent"
    elif average >= 85:
        return "Very Good"
    elif average >= 80:
        return "Good"
    elif average >= 75:
        return "Fair"
    else:
        return "Failed"


grades_SGB = []
for i in range(1, 4):
    grade = float(input(f"Enter grade {i}: "))
    grades_SGB.append(grade)

average = calculate_average(grades_SGB)
remark = get_remark(average)

print(f"Average Grade: {average:.2f}")
print(f"Remark: {remark}")
