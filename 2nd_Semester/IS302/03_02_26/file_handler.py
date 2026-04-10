from student import Student

FILENAME = "data.txt"

def save_student(student):
    with open("student.txt", "a") as f:
        f.write(student.to_file_format())

def load_students():
    students = []
    try:
        with open("student.txt", "r") as f:
            for line in f:
                name, age, student_id, course = line.strip().split(",")
                student = Student(name, int(age), student_id, course)
                students.append(student)

    except FileNotFoundError:
        pass
    return students