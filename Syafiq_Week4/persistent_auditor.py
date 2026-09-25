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
    for oid, amount, tax in history:
        print(f"{oid}, Amount={amount}, Tax={tax:.2f}") 

def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, "r") as f:
            print("Current Orders: \n")
            first_line = f.readline().strip()
            try:
                return int(first_line.split(":")[-1].strip())
            except ValueError:
                return 0
    else:
        return 0

def save_inventory():
    """Save final totals and transaction history to file."""
    with open(inventory_file, "w") as f:
        f.write(f"Final Inventory: {inventory}\n")
        f.write(f"Total Units Processed: {total_units_processed}\n")
        f.write(f"Total Deliveries Processed: {total_deliveries}\n")
        f.write(f"Failed/Rejected Entries: {failed_entries}\n")
        f.write("Transaction History:\n")
        for oid, amount, tax in history:
            f.write(f"{oid}, Amount={amount}, Tax={tax:.2f}\n")
    print(f"Inventory and history saved to {inventory_file}")

################ Start Program ################

inventory = load_inventory()

print("Persistent Auditor Started. Type 'quit' to exit." )
print(f"Starting Inventory: {inventory}")

while True:
    entry = get_valid_input()

    if entry == "quit":
        generate_report()
        save_inventory()
        break

    if entry is None:
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
    history.append((order_id, entry, tax))
    print(f"New Order Added: \n{order_id}, Amount={entry}, Tax={tax:.2f}")
    
    order_id += 1

    print(f"Quantity added. Current inventory: {inventory}")

    if inventory > 500:
        print("ALERT: Inventory exceeded 500 units. Stopping auditor immediately.")
        generate_report()
        save_inventory()
        break


