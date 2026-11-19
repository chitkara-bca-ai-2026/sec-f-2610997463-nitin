inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("=" * 50)
print("INVENTORY CONTROL SYSTEM")
print("=" * 50)

while True:
    print()
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    print()

    choice = "".join(input("Enter your choice (1-5): ").split())

    if choice == "1":
        print()
        print("--- Current Inventory ---")
        for i in range(len(inventory)):
            print(f"{i+1}. {inventory[i]}")

    elif choice == "2":
        item = "".join(input("Enter item name to add: ").split())
        if item:
            inventory.append(item)
            print(f'[SUCCESS] "{item}" added to inventory.')
        else:
            print("[ERROR] Item name cannot be empty.")

    elif choice == "3":
        item = "".join(input("Enter item name to remove: ").split())
        if item in inventory:
            inventory.remove(item)
            print(f'[SUCCESS] "{item}" removed from inventory.')
        else:
            print(f'[ERROR] "{item}" not found in inventory.')

    elif choice == "4":
        inventory.sort()
        print()
        print("[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for i in range(len(inventory)):
            print(f"{i+1}. {inventory[i]}")

    elif choice == "5":
        print("Goodbye! Exiting Inventory System.")
        break

    else:
        print("[ERROR] Invalid choice! Please enter 1 to 5.")