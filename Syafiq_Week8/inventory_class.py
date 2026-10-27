# Manage Collection of Products objects.
import json
import os
from product_class import Product

class Inventory:
    FILENAME = "inventory.json"
    def __init__(self):
        self.products = [] #List to store Product objects

    def add_product(self):
        """Ask for the details of a new product and add it to the inventory."""
        print("\nAdd New Product")
        product_id = input("Product ID: ").strip().upper()
        if not product_id:
            print("\nProduct ID cannot be empty.")
            return
        if self.search_product(product_id):
            print("\nProduct ID already exists. Product not added.")
            return

        name = input("Product Name: ").strip()
        if not name:
            print("\nProduct name cannot be empty.")
            return

        uprice = input("Price: ").strip()
        ustock = input("Stock Quantity: ").strip()
        price = float(uprice) if uprice else 0.0
        stock = int(ustock) if ustock else 0

        self.products.append(Product(product_id, name, price, stock))
        print("\nProduct Added Successfully!")

    def search_product(self, product_id):
        product_id = product_id.strip().upper()
        for product in self.products:
            if product.get_product_id().upper() == product_id:
                return product
        return None

    def display_all(self):
        if not self.products:
            print("No Products in inventory!")
        else:
            for product in self.products:
                print(f"ID: {product.get_product_id()} | Name: {product.get_name()} | Price: ${product.get_price():.2f} | Stock: {product.get_stock()}")

    def load_inventory(self):
        """Load products from inventory.json if it exists."""
        if not os.path.exists(self.FILENAME):
            print(f"{self.FILENAME} not found. Starting with an empty inventory.")
            return
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
            self.products = [
                Product(d["id"], d["name"], d["price"], d["stock"])
                for d in data
            ]
            print("Inventory loaded successfully!")
        except (json.JSONDecodeError, OSError, TypeError, KeyError):
            print("Could not read the inventory file. Starting with an empty inventory.")
            self.products = []

    def save_inventory(self):
        """Write all products to inventory.json. Returns True on success."""
        try:
            data = [product.to_dict() for product in self.products]
            with open(self.FILENAME, "w") as file:
                json.dump(data, file, indent=4)
            return True
        except OSError:
            print(f"Error: Could not write to {self.FILENAME}.")
            return False

