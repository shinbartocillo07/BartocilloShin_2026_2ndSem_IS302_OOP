class employee():
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

emp1 = employee("Natsu", 22, 1000, 1234)
emp2 = employee("Goku", 23, 2000, 2234)
emp3 = employee("Luffy", 19, 4000, 3345)
emp4 = employee("Saitama", 20, 3000, 4456)
print(emp1.__dict__)
print(emp2.__dict__)
print(emp3.__dict__)
print(emp4.__dict__)


