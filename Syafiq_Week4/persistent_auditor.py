import os

inventory_file = "inventory.txt"

max_capacity = 1000
tax_rate = 0.10

inventory = 0
failed_entries = 0
total_units_processed = 0
total_deliveries = 0
history = []
 
def get_valid_input():
    entry = input("Enter Stock Quantity: ")

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
    print("Transaction History: ", history)  
    #print("Total Tax Amount: ")

if os.path.exists(inventory_file):
    with open(inventory_file, "r") as f:
        try:
            inventory = int(f.read().strip())
        except ValueError:
            inventory = 0
else:
    inventory = 0

################ Start Program ################

print("Persistent Auditor Started. Type 'quit' to exit." )
print(f"Starting Inventory: {inventory}")

while True:
    
    entry = get_valid_input()

    if entry == "quit":
        generate_report()
        with open(inventory_file, "w") as f:
                f.write(str(inventory))
        print(f"Inventory saved to {inventory_file}")
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
    history.append(entry)

    tax = calculate_tax(entry)
    print(f"Stock added. Current inventory: {inventory}") 
    print(f"Tax for this delivery: {tax:.2f}")

    if inventory > 500:
        print("ALERT: Inventory exceeded 500 units. Stopping auditor immediately.")
        generate_report()

        with open(inventory_file, "w") as f:
            f.write(str(inventory))
        print(f"Inventory saved to {inventory_file}")
        break


