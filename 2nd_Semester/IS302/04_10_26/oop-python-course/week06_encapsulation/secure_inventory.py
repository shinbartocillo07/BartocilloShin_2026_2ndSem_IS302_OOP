class Product_SGB:
    def __init__(self_SGB, name_SGB, price_SGB, quantity_SGB):
        self_SGB.__name_SGB = name_SGB
        self_SGB.__price_SGB = price_SGB
        self_SGB.__quantity_SGB = quantity_SGB

    def get_product_info_SGB(self_SGB):
        print("Product:", self_SGB.__name_SGB)
        print("Price:", self_SGB.__price_SGB)
        print("Quantity:", self_SGB.__quantity_SGB)

    def update_quantity_SGB(self_SGB, new_quantity_SGB):
        if new_quantity_SGB >= 0:
            self_SGB.__quantity_SGB = new_quantity_SGB

    def update_price_SGB(self_SGB, new_price_SGB):
        if new_price_SGB > 0:
            self_SGB.__price_SGB = new_price_SGB

# Example usage
product_SGB = Product_SGB("Laptop", 45000, 10)
product_SGB.get_product_info_SGB()