class Employee_SGB:
    def __init__(self_SGB, name_SGB):
        self_SGB.__name_SGB = name_SGB
        self_SGB.__salary_SGB = 0

    def set_salary_SGB(self_SGB, salary_SGB):
        if salary_SGB > 0:
            self_SGB.__salary_SGB = salary_SGB

    def get_salary_SGB(self_SGB):
        return self_SGB.__salary_SGB

emp_SGB = Employee_SGB("Ana")
emp_SGB.set_salary_SGB(30000)
print("Salary:", emp_SGB.get_salary_SGB())