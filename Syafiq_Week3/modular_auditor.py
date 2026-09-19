max_capacity = 1000
tax_rate = 0.10

inventory = 0
failed_entries = 0
total_units_processed = 0
total_deliveries_processed = 0
delivery_amount = 0
 
def get_valid_input():
    entry = input("Enter Stock Quantity: ")

    if entry.lower() == "quit":
        return "quit"

        try:
            quantity = int(entry)
        except ValueError:
            print("Error: Please enter a valid integer.")
            failed_entries += 1
            return None

    if quantity < 0:
        print("Error: Negative values are not allowed.")
        failed_entries += 1
        return None
        
    if inventory + quantity > max_capacity:
        print(f"Error: Adding {quantity} exceeds storage Capacity. {max_capacity}")
        failed_entries += 1
        return None
        
    inventory += quantity
    total_units_processed += quantity


def calculate_tax(amount):
    return amount * tax_rate

def generate_report():
    print("==========Report==========")
    print("Final Inventory: ", inventory)
    print("Total Units Processed: ", total_units_processed)
    print("Total Deliveries Processed: ", total_deliveries_processed)
    print("Failed/Rejected Entries: ", failed_entries)    
        


print("Inventory Auditor Started. Type 'quit' to exit." )

while True:
    
    entry = get_valid_input()

    print(f"stock added. Current inventory: {inventory}") 

    if inventory > 500:
        print("ALERT: Inventory exceeded 500 units. Stopping auditor immediately.")
        print("\n--- Report ---")
        print("Final Inventory:", inventory)
        print("Total Units Processed:", total_units_processed)
        print("Failed/Rejected Entries:", failed_entries)
        break


