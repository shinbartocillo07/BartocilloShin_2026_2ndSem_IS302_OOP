from student import Student
import file_handler as fh

def add_student():
    try:
        student_id = input("Enter Student ID: ").strip()
        if not student_id:
            raise ValueError("Student ID cannot be empty.")
        name = input("Enter Name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        course = input("Enter Course: ").strip()
        if not course:
            raise ValueError("Course cannot be empty.")
        student = Student(student_id, name, course)
        fh.save_student(student)
        print("Student added successfully")
    except Exception as e:
        print("Error adding student:", e)

def view_students():
    students = fh.view_students()
    if not students:
        print("No records found.")
        return
    print("\nStudents:")
    for s in students:
        print(s.display_info())

def search_student():
    search_id = input("Enter Student ID to search: ").strip()
    if not search_id:
        print("No ID entered.")
        return
    s = fh.search_student(search_id)
    if s:
        print("Student Found:")
        print(s.display_info())
    else:
        print("Student not found")

def main():
    while True:
        print("\nSTUDENT INFORMATION SYSTEM")
        print("1 Add Student")
        print("2 View Students")
        print("3 Search Student")
        print("4 Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
