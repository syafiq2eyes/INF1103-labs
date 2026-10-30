import json
import os
from product_class import Product

class File_Handling:
    FILENAME = "inventory.json"

    def load_inventory(self):
        """Return a list of Product objects from the file ([] if none)."""
        if not os.path.exists(self.FILENAME):
            print(f"{self.FILENAME} not found. Starting with an empty inventory.")
            return []
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
            products = [
                Product(d["id"], d["name"], d["price"], d["stock"])
                for d in data
            ]
            print("Inventory loaded successfully!")
            return products
        except (json.JSONDecodeError, OSError, TypeError, KeyError):
            print("Could not read the inventory file. Starting with an empty inventory.")
            return []

    def save_inventory(self, products):
        """Write the given products to inventory.json. Returns True on success."""
        try:
            data = [product.to_dict() for product in products]
            with open(self.FILENAME, "w") as file:
                json.dump(data, file, indent=4)
            return True
        except OSError:
            print(f"Error: Could not write to {self.FILENAME}.")
            return False