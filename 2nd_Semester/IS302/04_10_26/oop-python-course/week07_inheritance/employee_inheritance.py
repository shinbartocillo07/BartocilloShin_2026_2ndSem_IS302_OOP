class Employee_SGB:
    def __init__(self_SGB, name_SGB, salary_SGB):
        self_SGB.name_SGB = name_SGB
        self_SGB.salary_SGB = salary_SGB

class Manager_SGB(Employee_SGB):
    def __init__(self_SGB, name_SGB, salary_SGB, department_SGB):
        super().__init__(name_SGB, salary_SGB)
        self_SGB.department_SGB = department_SGB

    def display_manager_SGB(self_SGB):
        print("Name:", self_SGB.name_SGB)
        print("Salary:", self_SGB.salary_SGB)
        print("Department:", self_SGB.department_SGB)

manager1_SGB = Manager_SGB("John", 50000, "IT")
manager1_SGB.display_manager_SGB()