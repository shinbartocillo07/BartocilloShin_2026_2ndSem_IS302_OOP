class Person:
    def __init__(self, name, age):
        self.name_SGB = name
        self.age = age

    def display_info(self):
        print("Name:", self.name_SGB)
        print("Age:", self.age)


p1 = Person("Juan", 20)
p1.display_info()
