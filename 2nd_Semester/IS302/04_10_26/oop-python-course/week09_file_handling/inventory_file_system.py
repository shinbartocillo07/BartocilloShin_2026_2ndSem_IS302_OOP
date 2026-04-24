product_SGB = input("Enter product name: ")
price_SGB = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product_SGB + "," + price_SGB + "\n")

print("Product saved successfully")