inventory = 0
max_capacity = 1000
failed_entries = 0
total_units_processed = 0


print("Inventory Auditor Started. Type 'quit' to exit." )

while True:
    entry = input("Enter Stock Quantity:")

    if entry.lower() == "quit":
        print("Final Inventory:", inventory)
        print("Total Units Processed:", total_units_processed)
        print("Failed/Rejected Entries:", failed_entries)
        break

    if not entry.isdigit():
        print("Error: Please enter a valid positive integer.")
        failed_entries += 1
        continue

    quantity = int(entry)


    if quantity < 0:
        print("Error: Negative values are not allowed.")
        failed_entries += 1
        continue
    if inventory + quantity > max_capacity:
        print(f"Error: Adding {quantity} exceeds storage Capacity. {max_capacity}")
        failed_entries += 1
        continue

    inventory += quantity
    total_units_processed += quantity
    print(f"stock added. Current inventory: {inventory}") 

    if inventory > 500:
        print("ALERT: Inventory exceeded 500 units. Stopping auditor immediately.")
        print("\n--- Report ---")
        print("Final Inventory:", inventory)
        print("Total Units Processed:", total_units_processed)
        print("Failed/Rejected Entries:", failed_entries)
        break


