class Person_SGB:
    def __init__(self_SGB, name_SGB, age_SGB):
        self_SGB.__name_SGB = name_SGB
        self_SGB.__age_SGB = age_SGB

    def get_name_SGB(self_SGB):
        return self_SGB.__name_SGB

    def get_age_SGB(self_SGB):
        return self_SGB.__age_SGB

p1_SGB = Person_SGB("Maria", 20)
print("Name:", p1_SGB.get_name_SGB())
print("Age:", p1_SGB.get_age_SGB())