class Person:

    def __init__(self, name, age):
        self._name = name          
        self._age = age

    def display_info(self):
        return f"Name: {self._name}, Age: {self._age}"

Person1 = Person("", 22)
print(Person1.display_info())

