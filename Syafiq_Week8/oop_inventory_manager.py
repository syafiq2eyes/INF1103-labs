from product_class import Product
from inventory_class import Inventory
from file_handling import File_Handling

DIVIDER = "=" * 40
LINE = "-" * 48

################################### Menu System ###################################

print(f"\n{DIVIDER}")
print("INVENTORY MANAGEMENT SYSTEM")
print(f"\n{DIVIDER}")
print()

file_handler = File_Handling() #Create the inventory object form File_Handling Class
inventory = Inventory(file_handler.load_inventory())

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
        inventory.add_product()

    elif choice == "3":
        user_update_stock_productID = input("Enter Product ID to update stock: ")
        user_update_stock = int(input("Enter Quantity to update stock: "))

        found_product = inventory.search_product(user_update_stock_productID)
        if found_product:
            found_product.update_stock(user_update_stock)
            print("Stock updated successfully.")
        else:
            print("Product not found.")

    elif choice == "4":
        user_search_product = input("Enter Product ID to search: ")
        found_product = inventory.search_product(user_search_product)
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

    else:
        print("\nInvalid Option. Please enter a number from 1 to 6.")

