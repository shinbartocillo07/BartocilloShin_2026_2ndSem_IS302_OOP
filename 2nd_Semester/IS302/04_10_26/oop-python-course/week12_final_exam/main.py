from product import Product
import inventory_manager as im

def add_product():
    try:
        product_id = input("Enter Product ID: ").strip()
        if not product_id:
            raise ValueError("Product ID cannot be empty")
        name = input("Enter Product Name: ").strip()
        if not name:
            raise ValueError("Product Name cannot be empty")
        price = float(input("Enter Price: ").strip())
        quantity = int(input("Enter Quantity: ").strip())
        product = Product(product_id, name, price, quantity)
        im.add_product(product)
        print("Product added successfully")
    except ValueError as e:
        print("Invalid input:", e)
    except Exception as e:
        print("Error adding product:", e)

def view_products():
    products = im.view_products()
    if not products:
        print("No products found.")
        return
    print("\nProducts:")
    for p in products:
        print(p.get_product_info())

def search_product():
    pid = input("Enter Product ID: ").strip()
    if not pid:
        print("No ID entered.")
        return
    p = im.search_product(pid)
    if p:
        print("Product Found:")
        print(p.get_product_info())
    else:
        print("Product not found")

def update_quantity():
    pid = input("Enter Product ID to update: ").strip()
    if not pid:
        print("No ID entered.")
        return
    try:
        qty = int(input("Enter new quantity: ").strip())
    except ValueError:
        print("Invalid quantity")
        return
    ok = im.update_quantity(pid, qty)
    if ok:
        print("Quantity updated")
    else:
        print("Product not found; quantity not updated")

def main():
    while True:
        print("\nINVENTORY MANAGEMENT SYSTEM")
        print("1 Add Product")
        print("2 View Products")
        print("3 Search Product")
        print("4 Update Quantity")
        print("5 Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_quantity()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
