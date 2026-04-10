from person import Person

class Student(Person):
    def __init__(self, name, age, student_id, course):
        self().__init__(name, age)
        self._student_id = student_id
        self._course = course

    def get_student_id(self):
        return self._student_id

    def get_course(self):
        return self._course

# Method overriding
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, ID: {self._student_id}, Course: {self._course}"

    def to_file_format(self):
        return f"{self._name},{self._age},{self._student_id},{self._course}"

