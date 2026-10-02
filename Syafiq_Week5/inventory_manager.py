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

###################################Inventory Management###################################

def load_inventory():
    """Load Inventory.json if it exists. Otherwise begin with an empty list."""
    if not os.path.exists(FILENAME):
        print(f"{FILENAME} not found. Starting with an empty inventory.")
        return []
    print(f"{FILENAME} found! ")
    try:  
        with open(FILENAME, "r") as file:
            inventory = json.load(file)
        for product in inventory:
            ####
            product.setdefault("history", [product["stock"]])

    except (json.JSONDecodeError, OSError, TypeError, KeyError, AttributeError):
        print("Could not read the inventory file. Starting with an empty inventory.")
        return []

    print("Inventory Loaded Successfully!")
    return []


def save_inventory(inventory):
    """Write the inventory list to inventory.json Returns True on success."""
    try:
        with open(FILENAME, "w") as file:
            json.dump(inventory, file, indent=4)
        return True
    except OSError:
        print(f"Error: Could not write to {FILENAME}.")
        return False


######################################################################

## Data Manipulation

def add_product(inventory):
    """Ask for the details of a new product and add it to the inventory."""
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip().upper()
    if not product_id:
        print("\nProduct ID cannot be empty.")
        return
    if find_product(inventory, product_id):
        print("\nProduct ID already exists. Product not added.")
        return

    name = input("Product Name: ").strip()
    if not name:
        print("\nProduct name cannot be empty.")
        return
    price = get_number("Price: ", float)
    stock = get_number("Stock Quantity: ", int)

    inventory.append({
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock,
        "history": [stock],
    })
    print("\nProduct Added Successfully!")

def update_stock(inventory):
    """Find a product by ID and set a new stock quantity."""
    print("\nUpdate Stock")
    product = find_product(inventory, input("Enter Product ID:"))
    if product is None:
        print("\nProduct not found! ")
        return

    print("\nProuct Found: ")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    print()
    new_stock = get_number("New Stock Quantity: ", int)

    #Record how much the stock changed by, then update the running total
    product["history"].append(new_stock - product["stock"])
    product["stock"] = new_stock
    print("\nStock updated successfully!")
    









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




