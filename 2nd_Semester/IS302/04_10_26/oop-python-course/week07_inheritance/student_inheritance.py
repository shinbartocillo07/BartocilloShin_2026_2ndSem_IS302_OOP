class Person_SGB:
    def __init__(self_SGB, name_SGB, age_SGB):
        self_SGB.name_SGB = name_SGB
        self_SGB.age_SGB = age_SGB

class Student_SGB(Person_SGB):
    def __init__(self_SGB, name_SGB, age_SGB, course_SGB):
        super().__init__(name_SGB, age_SGB)
        self_SGB.course_SGB = course_SGB

    def display_student_SGB(self_SGB):
        print("Name:", self_SGB.name_SGB)
        print("Age:", self_SGB.age_SGB)
        print("Course:", self_SGB.course_SGB)

student1_SGB = Student_SGB("Maria", 20, "BSIS")
student1_SGB.display_student_SGB()