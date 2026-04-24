class Animal_SGB:
    def __init__(self_SGB, name_SGB):
        self_SGB.name_SGB = name_SGB

    def speak(self_SGB):
        print(self_SGB.name_SGB, "makes a sound")

class Dog_SGB(Animal_SGB):
    def bark(self_SGB):
        print(self_SGB.name_SGB, "barks")

dog1_SGB = Dog_SGB("Buddy")
dog1_SGB.speak()
dog1_SGB.bark()