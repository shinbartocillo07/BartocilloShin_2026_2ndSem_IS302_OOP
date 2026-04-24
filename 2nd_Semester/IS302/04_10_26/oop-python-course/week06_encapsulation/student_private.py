class Student_SGB:
    def __init__(self_SGB, name_SGB, student_id_SGB, gpa_SGB):
        self_SGB.__name_SGB = name_SGB
        self_SGB.__student_id_SGB = student_id_SGB
        self_SGB.__gpa_SGB = gpa_SGB

    def get_student_info_SGB(self_SGB):
        print("Name:", self_SGB.__name_SGB)
        print("Student ID:", self_SGB.__student_id_SGB)
        print("GPA:", self_SGB.__gpa_SGB)

student1_SGB = Student_SGB("Juan", "2023-001", 1.75)
student1_SGB.get_student_info_SGB()