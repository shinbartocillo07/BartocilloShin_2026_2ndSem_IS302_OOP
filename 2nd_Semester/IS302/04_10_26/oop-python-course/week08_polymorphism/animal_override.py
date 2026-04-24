class Animal_SGB:
    def speak_SGB(self_SGB):
        print("Animal makes a sound")

class Dog_SGB(Animal_SGB):
    def speak_SGB(self_SGB):
        print("Dog barks")

class Cat_SGB(Animal_SGB):
    def speak_SGB(self_SGB):
        print("Cat meows")

animals_SGB = [Dog_SGB(), Cat_SGB()]
for animal_SGB in animals_SGB:
    animal_SGB.speak_SGB()