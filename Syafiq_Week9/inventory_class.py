# Manage Collection of Products objects.
import math
from product_class import Product
from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct

def get_number(prompt, cast, minimum=0):
    """Keep asking until the user enters a valid, non-negative number."""
    while True:
        try:
            value = cast(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter a valid number.")
            continue
        if not math.isfinite(value):
            print("Invalid Input. Please enter a number.")
            continue
        if value < minimum:
            print(f"Invalid Input. Please enter a number greater than or equal to {minimum}.")
            continue
        return value

class Inventory:
    def __init__(self, products=None):
        self.products = products or [] #List to store Product objects

    def add_product(self):
        """Ask for the details of a new product and add it to the inventory."""
        print("\nAdd New Product")
        print("1. Physical Product")
        print("2. Digital Product")
        kind = input("Choose product type (1 or 2): ").strip()
        if kind not in ("1", "2"):
            print("Invalid choice. Product not added.")
            return

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

        price = get_number("Price: ", float)
        stock = get_number("Stock Quantity: ", int)

        if kind == "1":
            weight = get_number("Weight (kg): ", float)
            product = PhysicalProduct(product_id, name, price, stock, weight)

        else:
            download_size = get_number("Download Size (MB): ", float)
            product = DigitalProduct(product_id, name, price, stock, download_size)

        self.products.append(product)
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
                product.display_information()

