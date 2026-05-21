import os
from product import Product

PRODUCTS_FILE = os.path.join(os.path.dirname(__file__), "products.txt")

def add_product(product):
    with open(PRODUCTS_FILE, "a", encoding="utf-8") as f:
        f.write(product.get_product_info() + "\n")

def view_products():
    try:
        products = []
        with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    p = Product.from_csv(line)
                    products.append(p)
                except Exception:
                    continue
        return products
    except FileNotFoundError:
        return []

def search_product(product_id):
    try:
        with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    p = Product.from_csv(line)
                except Exception:
                    continue
                if p.get_id() == product_id:
                    return p
        return None
    except FileNotFoundError:
        return None

def update_quantity(product_id, new_quantity):
    products = view_products()
    updated = False
    for p in products:
        if p.get_id() == product_id:
            p.update_quantity(new_quantity)
            updated = True
            break
    if not updated:
        return False
    # write back all products
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        for p in products:
            f.write(p.get_product_info() + "\n")
    return True
