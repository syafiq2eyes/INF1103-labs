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

def search_product(inventory):
    """Find a product by ID and show its details."""
    print("\nSearch Product")
    product = find_product(inventory, input("Enter Product ID: "))
    if product is None:
        print("\n Product was not found. :(")
        return

    print("\nProduct Found!")
    print(LINE)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: {product['price']:.2sf}")
    print(f"Stock: {product['stock']}")
    print(LINE)

def display_all(inventory):
    """show every product in the inventory."""
    print("\nCurrent Inventory")
    print(LINE)
    if not inventory:
        print("No Products in inventory.")
    for product in inventory:
        print(
            f"ID: {product['id']} | Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | Stock: {product['stock']}"
        )
    print(LINE)

###################################Menu System###################################

print(f"\n{DIVIDER}")
print("INVENTORY MANAGEMENT SYSTEM")
print(f"\n{DIVIDER}")
print()

inventory = load_inventory()

print("\n---------- MENU ----------")
print("1. Display All Products")
print("2. Add Product")
print("3. Update Stock")
print("4. Search Product")
print("5. Save Inventory")
print("6. Exit")
print("----------------------------")

while True:
    choice = input("\nEnter Option: ").strip()

    if choice == "1":
        display_all(inventory)

    elif choice == "2":
        add_product(inventory)
    
    elif choice == "3":
        update_stock(inventory)

    elif choice == "4":
        search_product(inventory)

    elif choice == "5":
        print("\nSaving Inventory...")
        if save_inventory(inventory):
            print(f"Inventory has been saved successfully to {FILENAME}")

    elif choice == "6":
        print("\nSaving inventory before exit...")
        if save_inventory(inventory):
            print("Inventory saved successfully.")
        print("\nThank you for using Inventory Management System.")
        print("Program Terminated.")
        break

    else:
        print("\nInvalid Option. PLease enter a number from 1 to 6.")




