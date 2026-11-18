import csv
from inventory_class import Inventory
from ProductFactory import ProductFactory
from Supplier import Supplier

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader, None)
            for row_number, row in enumerate(reader, start=2):
                try:
                    product_type, product_id, name, price, stock = row
                    product = ProductFactory.create(
                        product_type, product_id, name,
                        float(price), int(stock), supplier, 0.0)
                    if inventory.add_product(product):
                        loaded += 1
                    else:
                        print(f"Row {row_number} skipped: duplicate ID {product_id}")
                except ValueError as error:
                    print(f"Row {row_number} skipped: {error}")

        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")