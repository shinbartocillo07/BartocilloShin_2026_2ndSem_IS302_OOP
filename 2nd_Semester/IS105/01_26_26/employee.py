class employee():
    def __init__(self, name, age, id, salary):
        self.name = name
        self.salary = salary
        self.id = id

emp1 = employee("harshit", 22, 1000, 1234)
emp2 = employee("arjun", 23, 2000, 2234)
print(emp1.__dict__)