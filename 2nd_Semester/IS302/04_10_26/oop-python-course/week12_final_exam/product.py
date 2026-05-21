class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__product_id = str(product_id)
        self.__name = str(name)
        self.__price = float(price)
        self.__quantity = int(quantity)

    def get_product_info(self):
        return f"{self.__product_id},{self.__name},{self.__price},{self.__quantity}"

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def update_quantity(self, quantity):
        self.__quantity = int(quantity)

    @classmethod
    def from_csv(cls, csv_line):
        parts = csv_line.strip().split(",")
        if len(parts) != 4:
            raise ValueError("Invalid product record")
        pid = parts[0]
        name = parts[1]
        price = float(parts[2])
        qty = int(parts[3])
        return cls(pid, name, price, qty)
