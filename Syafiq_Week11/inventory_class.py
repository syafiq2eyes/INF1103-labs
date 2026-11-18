# Manage Collection of Products objects.
import math
from product_class import Product
from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from product_class import Product

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
    def __init__(self, products: list[Product] | None = None):
        self.products: list[Product] = products or [] # if no products are provided, Initialize with an empty list  

    def add_product(self, product: Product) -> bool:
        """Ask for the details of a new product and add it to the inventory."""
        if self.find_product(product.get_product_id()) is not None:
            return False # Product already exists
        self.products.append(product)
        return True

    def remove_product(self, product_id: str) -> Product | None:
        """Remove the reference from this inventory and return it."""
        product = self.find_product(product_id)
        if product is not None:
            self.products.remove(product)
        return product

    def find_product(self, product_id: str) -> Product | None:
        product_id = product_id.strip().upper()
        for product in self.products:
            if product.get_product_id().upper() == product_id:
                return product
        return None

    def display_all(self) -> None:
        if not self.products:
            print("No Products in inventory!")
            return
        for product in self.products:
            product.display_information()

