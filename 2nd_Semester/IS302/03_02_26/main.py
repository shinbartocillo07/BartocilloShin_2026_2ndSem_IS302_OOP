from student import Student
from file_handler import save_student, load_students

def display_menu():
        print("\n===== Student Information System =====")
        print("1 - Add Student")
        print("2 - View Students")
        print("3 - Exit")

def main():
        students = load_students()

        while True:
            display_menu()
            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                student_id = input("Enter student ID: ")
                course = input("Enter course: ")

                student = Student(name, age, student_id, course)
                students.append(student)
                save_student(student)

                print("Student added successfully!")

            elif choice == "2":
                if not students:
                    print("No students found.")
                else:
                    for student in students:
                     print(student.display_info())

            elif choice == "3":
                print("Exiting program...")
                break
        else:
                    print("Invalid choice. Please try again.")
if __name__=="__main__":
    main()
