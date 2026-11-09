from product_class import Product
from inventory_class import Inventory, get_number
from file_handling import File_Handling
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from CanBeShipped import CanBeShipped
from Supplier import Supplier
from OrderLine import OrderLine
from Order import Order

suppliers: dict[str, Supplier] = {} #allows several products to share the same supplier object

def choose_supplier() -> Supplier | None:
    supplier_id = input("Enter Supplier ID: ").strip().upper()
    if not supplier_id:
        print("\nSupplier ID cannot be empty.")
        return None
    if supplier_id in suppliers:
        print(f"Using existing supplier: {suppliers[supplier_id].get_name()}")
        return suppliers[supplier_id]

    name = input("Supplier Name: ").strip()
    email = input("Supplier Email: ").strip()
    if not name or not email:
        print("\nSupplier Name and Email cannot be empty.")
        return None
    supplier = Supplier(supplier_id, name, email)
    suppliers[supplier_id] = supplier
    return supplier

def add_product_menu(inventory: Inventory) -> None:
    print("\nAdd New Product")
    print("1. Physical product")
    print("2. Digital product")
    kind = input("Choose product type (1 or 2): ").strip()
    if kind not in ("1", "2"):
        print("\nInvalid product type. Product not added.")
        return

    product_id = input("Product ID: ").strip().upper()
    if not product_id:
        print("\nProduct ID cannot be empty.")
        return
    if inventory.find_product(product_id) is not None:
        print("\nProduct ID already exists. Product not added.")
        return

    name = input("Product Name: ").strip()
    if not name:
        print("\nProduct name cannot be empty.")
        return
    price = get_number("Price: ", float)
    stock = get_number("Stock Quantity: ", int)

    supplier = choose_supplier()
    if supplier is None:
        print("Product not added.")
        return

    product: Product
    if kind == "1":
        weight = get_number("Weight (kg): ", float)
        product = PhysicalProduct(product_id, name, price, stock, supplier, weight)
    else:
        download_size = get_number("Download Size (MB): ", float)
        product = DigitalProduct(product_id, name, price, stock, supplier, download_size)

    if inventory.add_product(product):
        print(f"\nProduct {product_id} added successfully.")
    else:
        print(f"\nFailed to add product {product_id}.")

DIVIDER = "=" * 40
LINE = "-" * 48

################################### Menu System ###################################

print(f"\n{DIVIDER}")
print("INVENTORY MANAGEMENT SYSTEM")
print(f"\n{DIVIDER}")
print()

file_handler = File_Handling() #Create the inventory object form File_Handling Class
inventory = Inventory(file_handler.load_inventory())

for product in inventory.products:
    supplier = product.get_supplier()
    suppliers[supplier.get_supplier_id()] = supplier  # Ensure suppliers are tracked

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
        inventory.display_all()

    elif choice == "2":
        add_product_menu(inventory)

    elif choice == "3":
        product = inventory.find_product(input("Enter Product ID to update stock: "))
        if product is None:
            print("Product not found.")
        else:
            new_stock = get_number("New Stock Quantity: ", int)
            product.update_stock(new_stock)
            print("Stock updated successfully.")

    elif choice == "4":
        user_search_product = input("Enter Product ID to search: ")
        found_product = inventory.find_product(user_search_product)
        if found_product:
            found_product.display_information()
        else:
            print("Product not found.")

    elif choice == "5":
        print("\nSaving Inventory...")
        if file_handler.save_inventory(inventory.products):
            print(f"Inventory has been saved successfully to {file_handler.FILENAME}")

    elif choice == "6":
        print("\nSaving inventory before exit...")
        if file_handler.save_inventory(inventory.products):
            print("Inventory saved successfully.")
        print("\nThank you for using Inventory Management System.")
        print("Program Terminated.")
        break

    elif choice == "7":
        #laptop = PhysicalProduct("P211", "Laptop", 1500.00, 5, 1.8)
        #ebook = DigitalProduct("D211", "E-Book", 15.00, 100, 200)

        #light = PhysicalProduct("P010", "Pen", 1.50, 10, 0.1)
        #medium = PhysicalProduct("P011", "Book", 12.00, 5, 1.0)
        #heavy = PhysicalProduct("P012", "Monitor", 250.00, 3, 6.5)

        supplier = Supplier("S005", "Tech NONO Inc.", "sales@techNONOsupplies.com")
        laptop = PhysicalProduct("P5005", "Laptop", 1500.00, 5, supplier, 1.8)
        ebook = DigitalProduct("D301", "E-Book", 19.90, 100, supplier, 12.5)

        order1 = Order("O001")
        order1.add_order_line(laptop, 2)
        order1.add_order_line(ebook, 1)
        order1.display_information()

        order2 = Order("O002")
        order2.add_order_line(laptop, 1)

        line1 = order1.get_order_lines()[0]
        line2 = order2.get_order_lines()[0]
        print(line1 is line2)
        print(line1.get_product() is line2.get_product())
        print(id(line1.get_product()), id(line2.get_product()))

        order1.remove_order_line("P5005")
        order1.display_information()
        laptop.display_information()
        order2.display_information()

        supplier = Supplier("S001", "TechSupply Co", "sales@techsupply.com")
        print("\n\n\n")
        inventory.add_product(PhysicalProduct("P005", "Monitor", 250.00, 3, supplier, 6.5))

        for product in inventory.products:
            product.display_information()
            print(product.get_fulfilment_info())
            print()


    #     for item in [laptop, ebook]:
    #         item.display_information()
    #         print(item.get_fulfilment_info())
    #         print()

    #     # for item in [light, medium, heavy]:
    #     #     print(f"{item.get_name()}: {item.get_weight()} kg, -> ${item.calculate_shipping_cost():.2f} shipping cost")

    #     try:
    #         CanBeShipped()
    #     except TypeError as error:
    #         print(error)  # This will raise an error because CanBeShipped is abstract and cannot be instantiated.


    #     print("===========")

        
        
    #     laptop.get_supplier().display_information()
    #     ebook.get_supplier().display_information()

    #     print(laptop.get_supplier() is ebook.get_supplier())  

    #     del supplier  # Delete the supplier reference
    #     laptop.get_supplier().display_information()
    #     ebook.get_supplier().display_information()

    #     sparesupplier = Supplier("S002", "Spare Parts Co.", "info@spare.com")
    #     sparesupplier.display_information()

    #     ebook.get_supplier().display_information()

    else:
        print("\nInvalid Option. Please enter a number from 1 to 6.")

    # inventory_a = Inventory()  
    # inventory_b = Inventory()

    # inventory_a.add_product(laptop)
    # print(inventory_a.find_product("S5005") is laptop)

    # removed = inventory_a.remove_product("S5005")
    # print(inventory_a.find_product("S5005"))
    # laptop.update_stock(10)
    # laptop.display_information()

    # inventory_b.add_product(laptop)
    # print(inventory_b.find_product("S5005") is laptop)  

    # inventory_b.products.clear()
    # laptop.display_information()  

