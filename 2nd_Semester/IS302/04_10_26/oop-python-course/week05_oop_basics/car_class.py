class Car:
    def __init__(self, brand, model, year):
        self.brand_SGB = brand
        self.model = model
        self.year = year

    def display_car(self):
        print(self.brand_SGB, self.model, self.year)


car1 = Car("Toyota", "Corolla", 2020)
car1.display_car()
