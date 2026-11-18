import json
import os
from Supplier import Supplier
from product_class import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

class File_Handling:
    FILENAME: str = "inventory.json"

    def load_inventory(self) -> list[Product]:
        """Return a list of Product objects from the file ([] if none)."""
        if not os.path.exists(self.FILENAME):
            print(f"{self.FILENAME} not found. Starting with an empty inventory.")
            return []
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read the inventory file. Starting with an empty inventory.")
            return []

        suppliers: dict[str, Supplier] = {}
        products: list[Product] = []
        for d in data:
            try:
                info = d["supplier"]
                supplier_id = info["supplier_id"]
                if supplier_id not in suppliers:
                    suppliers[supplier_id] = Supplier(supplier_id, info["name"], info["contact_email"])
                supplier = suppliers[supplier_id]

                if d["type"] == "physical":
                    products.append(PhysicalProduct(
                        d["id"], d["name"], d["price"], d["stock"], supplier, d["weight"]))
                elif d["type"] == "digital":
                    products.append(DigitalProduct(
                            d["id"], d["name"], d["price"], d["stock"], supplier, d["download_size"]))
                else:
                    print(f"Skipped {d.get('id', '?')}: unknown type '{d['type']}'.")
            except (KeyError, TypeError):
                print(f"Skipped an entry that is missing required fields or has invalid data.")
                

        print("Inventory Loaded Successfully!")    
        return products
    
    def save_inventory(self, products: list[Product]) -> bool:
        """Write the given products to inventory.json. Returns True on success."""
        try:
            data = [product.to_dict() for product in products]
            with open(self.FILENAME, "w") as file:
                json.dump(data, file, indent=4)
            return True
        except OSError:
            print(f"Error: Could not write to {self.FILENAME}.")
            return False