class Employee_SGB:
    def work_SGB(self_SGB):
        print("Employee performs tasks")

class Programmer_SGB(Employee_SGB):
    def work_SGB(self_SGB):
        print("Programmer writes code")

class Designer_SGB(Employee_SGB):
    def work_SGB(self_SGB):
        print("Designer creates UI designs")

employees_SGB = [Programmer_SGB(), Designer_SGB()]
for emp_SGB in employees_SGB:
    emp_SGB.work_SGB()