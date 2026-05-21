class Student:
    def __init__(self, student_id, name, course):
        self.student_id_SGB = student_id
        self.name_SGB = name
        self.course_SGB = course

    def display_info(self):
        return f"{self.student_id_SGB}, {self.name_SGB}, {self.course_SGB}"

    def to_csv(self):
        return f"{self.student_id_SGB},{self.name_SGB},{self.course_SGB}"

    def get_id(self):
        return self.student_id_SGB

    def get_name(self):
        return self.name_SGB

    def get_course(self):
        return self.course_SGB

    @classmethod
    def from_csv(cls, csv_line):
        parts = csv_line.strip().split(",")
        if len(parts) != 3:
            raise ValueError("Invalid record format")
        return cls(parts[0], parts[1], parts[2])
