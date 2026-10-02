import json
import math
import os

FILENAME = "inventory.json"
DIVIDER = "=" * 40
LINE = "-" * 48

def find_product(inventory, product_id):
    """Return the product with this ID (case-insensitive), or None."""
    for product in inventory:
        if product["id"].upper() == product_id:
            return product
    return None

def get_number(prompt, cast, minimum=0):
    """Keep asking until the user enters a valid, non-negative int/float."""
    while True:
        try:
            value = cast(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter a number.")
            continue
        if not math.isfinite(value):
            print("Invalid Input. Please enter a number.")
            continue
        if value < minimum:
            print(f"Value cannot be less than {minimum}.")
            continue
        return value





print(f"\n{DIVIDER}")
print("INVENTORY MANAGEMENT SYSTEM")
print(f"\n{DIVIDER}")

while True:
    print("-------MENU-------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------")
    break




