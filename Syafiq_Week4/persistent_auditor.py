import os

inventory_file = "inventory.txt"

max_capacity = 1000
tax_rate = 0.10

inventory = 0
failed_entries = 0
total_units_processed = 0
total_deliveries = 0
history = []
order_id = 1001

def get_product_name():
    product_name = input("\nEnter Product Name: ").strip()
    if product_name.lower() == "quit":
        return "quit"
    return product_name

def get_valid_input():
    entry = input("\nEnter Quantity: ")

    if entry.lower() == "quit":
        return "quit"

    try:
        quantity = int(entry)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return None

    if quantity < 0:
        print("Error: Negative values are not allowed.")
        return None

    return quantity

def calculate_tax(amount):
    return amount * tax_rate

def generate_report():
    print("==========Report==========")
    print("Final Inventory: ", inventory)
    print("Total Units Processed: ", total_units_processed)
    print("Total Deliveries Processed: ", total_deliveries)
    print("Failed/Rejected Entries: ", failed_entries)  
    print("Transaction History: ")
    for oid, pname, qty in history:
        print(f"{oid}, {pname} , {qty}") 

def load_inventory():
    last_order_id = 1000
    inventory_val = 0
    loaded_history = []
    if os.path.exists(inventory_file):
        with open(inventory_file, "r") as f:
            lines = f.readlines()
            print("Current Orders: \n")
            for line in lines:
                if "," in line:
                    parts = line.strip().split(",")
                    try:
                        oid = int(parts[0].strip())
                        pname = parts[1].strip()
                        qty = int(parts[2].strip())
                        loaded_history.append((oid, pname, qty))
                        last_order_id = max(last_order_id, oid)
                    except ValueError:
                        continue

            try: 
                first_line = lines[0].strip()
                inventory_val = int(first_line.split(":")[-1].strip())
            except Exception:
                inventory_val = 0
            return inventory_val, last_order_id, loaded_history
    else:
        return 0, last_order_id, loaded_history

def save_inventory():
    """Save final totals and transaction history to file."""
    with open(inventory_file, "w") as f:
        f.write(f"Final Inventory: {inventory}\n")
        f.write(f"Total Units Processed: {total_units_processed}\n")
        f.write(f"Total Deliveries Processed: {total_deliveries}\n")
        f.write(f"Failed/Rejected Entries: {failed_entries}\n")
        f.write("Transaction History:\n")
        for oid, pname, qty in history:
            f.write(f"{oid}, {pname}, {qty}\n")
    print(f"\nQuantity added. Current inventory: {inventory}")
    print(f"Order Successfully saved to {inventory_file}")
    



################ Start Program ################

inventory, last_order_id, history = load_inventory()
order_id = last_order_id + 1
print("Persistent Auditor Started. Type 'quit' to exit." )
print(f"Starting Inventory: {inventory}")

if history:
    print("Current Orders: ")
    for oid, pname, qty in history:
        print(f"{oid}, {pname}, {qty}")

while True:
    product_name = get_product_name()
    if product_name == "quit":
        generate_report()
        save_inventory()
        break 
    entry = get_valid_input()
    if entry == "quit":
        generate_report()
        save_inventory()
        break

    if entry is None or not product_name:
        failed_entries += 1
        continue

    if inventory + entry > max_capacity:
        print(f"Error: Adding {entry} exceeds storage Capacity. {max_capacity}")
        failed_entries += 1
        continue
        
    inventory += entry
    total_units_processed += entry
    total_deliveries += 1

    tax = calculate_tax(entry)
    history.append((order_id, product_name, entry))
    print(f"New Order Added: \n{order_id}, {product_name}, {entry}")
    
    order_id += 1

    print(f"\nQuantity added. Current inventory: {inventory}")
    print("Order Successfully saved to inventory.txt")

    if inventory > 500:
        print("ALERT: Inventory exceeded 500 units. Stopping auditor immediately.")
        generate_report()
        save_inventory()
        break


