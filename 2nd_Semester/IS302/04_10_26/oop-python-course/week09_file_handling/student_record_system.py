name_SGB = input("Enter student name: ")
course_SGB = input("Enter course: ")
with open("students.txt", "a") as file_SGB:
    file_SGB.write(name_SGB + "," + course_SGB + "\n")

print("\nStudent Records")
with open("students.txt", "r") as file_SGB:
    for line_SGB in file_SGB:
        print(line_SGB.strip())
