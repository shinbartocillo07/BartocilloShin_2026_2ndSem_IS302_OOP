import os
from student import Student

DATA_FILE = os.path.join(os.path.dirname(__file__), "students.txt")

def save_student(student):
    try:
        with open(DATA_FILE, "a", encoding="utf-8") as f:
            f.write(student.to_csv() + "\n")
    except Exception:
        raise

def view_students():
    try:
        students = []
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    s = Student.from_csv(line)
                    students.append(s)
                except ValueError:
                    continue
        return students
    except FileNotFoundError:
        return []

def search_student(student_id):
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    s = Student.from_csv(line)
                except ValueError:
                    continue
                if s.get_id() == student_id:
                    return s
        return None
    except FileNotFoundError:
        return None
