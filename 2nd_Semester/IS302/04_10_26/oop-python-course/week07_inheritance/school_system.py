class Person_SGB:
    def __init__(self_SGB, name_SGB, age_SGB):
        self_SGB.name_SGB = name_SGB
        self_SGB.age_SGB = age_SGB

    def display_info_SGB(self_SGB):
        print("Name:", self_SGB.name_SGB)
        print("Age:", self_SGB.age_SGB)

class Student_SGB(Person_SGB):
    def __init__(self_SGB, name_SGB, age_SGB, course_SGB):
        super().__init__(name_SGB, age_SGB)
        self_SGB.course_SGB = course_SGB

    def display_info_SGB(self_SGB):
        super().display_info_SGB()
        print("Course:", self_SGB.course_SGB)

class Teacher_SGB(Person_SGB):
    def __init__(self_SGB, name_SGB, age_SGB, subject_SGB):
        super().__init__(name_SGB, age_SGB)
        self_SGB.subject_SGB = subject_SGB

    def display_info_SGB(self_SGB):
        super().display_info_SGB()
        print("Subject:", self_SGB.subject_SGB)

# Example usage
student_SGB = Student_SGB("Maria", 20, "BSIS")
teacher_SGB = Teacher_SGB("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_SGB.display_info_SGB()
print("\nTeacher Info:")
teacher_SGB.display_info_SGB()