class Vehicle_SGB:
    def __init__(self_SGB, brand_SGB, model_SGB):
        self_SGB.brand_SGB = brand_SGB
        self_SGB.model_SGB = model_SGB

class Car_SGB(Vehicle_SGB):
    def __init__(self_SGB, brand_SGB, model_SGB, year_SGB):
        super().__init__(brand_SGB, model_SGB)
        self_SGB.year_SGB = year_SGB

    def display_car_SGB(self_SGB):
        print(self_SGB.brand_SGB, self_SGB.model_SGB, self_SGB.year_SGB)

car1_SGB = Car_SGB("Toyota", "Corolla", 2022)
car1_SGB.display_car_SGB()