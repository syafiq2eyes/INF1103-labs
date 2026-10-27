# Manage Collection of Products objects.
import json
import os
from product_class import Product

class Inventory:
    
    def __init__(self, products=None):
        self.products = products or [] #List to store Product objects

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

