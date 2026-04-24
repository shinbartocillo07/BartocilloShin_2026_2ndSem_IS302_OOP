import math

class Shape_SGB:
    def area_SGB(self_SGB):
        pass  # Placeholder for polymorphism

class Rectangle_SGB(Shape_SGB):
    def __init__(self_SGB, width_SGB, height_SGB):
        self_SGB.width_SGB = width_SGB
        self_SGB.height_SGB = height_SGB

    def area_SGB(self_SGB):
        return self_SGB.width_SGB * self_SGB.height_SGB

class Circle_SGB(Shape_SGB):
    def __init__(self_SGB, radius_SGB):
        self_SGB.radius_SGB = radius_SGB

    def area_SGB(self_SGB):
        return math.pi * self_SGB.radius_SGB ** 2

class Triangle_SGB(Shape_SGB):
    def __init__(self_SGB, base_SGB, height_SGB):
        self_SGB.base_SGB = base_SGB
        self_SGB.height_SGB = height_SGB

    def area_SGB(self_SGB):
        return 0.5 * self_SGB.base_SGB * self_SGB.height_SGB

# Example usage
rectangle_SGB = Rectangle_SGB(10, 5)
circle_SGB = Circle_SGB(5)
triangle_SGB = Triangle_SGB(8, 6)

print(f"Rectangle Area: {rectangle_SGB.area_SGB()}")
print(f"Circle Area: {circle_SGB.area_SGB():.1f}")
print(f"Triangle Area: {triangle_SGB.area_SGB()}")
