class GroceryStoreInventory:
    def __init__(self):
        self.inventory = {}

    # ADD NEW ITEMS TO THE INVENTORY

    def add_item(self, name, quantity, price):
        if name in self.inventory:
            print(f"Item '{name}' already exists in the inventory. Use 'update_item' to change quantity.")
        else:
            self.inventory[name] = (quantity, price)
            print(f"Item '{name}' added to the inventory.")

    # UPDATE EXISTING  ITEMS'  

    def update_item(self, name, quantity, price):
        if name in self.inventory:
            current_quantity, current_price = self.inventory[name]
            self.inventory[name] = (current_quantity + quantity,current_price + price)
            print(f"Quantity of '{name}' updated to {self.inventory[name][0]}.")
        else:
            print(f"Item '{name}' not found in the inventory. Use 'add_item' to add a new item.")

   # VIEW THE CURRENT INVENTORY        

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            print("{:<15} {:<10} {:<10}".format("Item", "Quantity", "Price"))
            print("-" * 35)
            for item, (quantity, price) in self.inventory.items():
                print("{:<15} {:<10} ₹{:<10.2f}".format(item, quantity, price))

    #REMOVE ITEMS FROM THE INVENTORY            

    def remove_item(self, name):
        if name in self.inventory:
            del self.inventory[name]
            print(f"Item '{name}' removed from the inventory.")
        else:
            print(f"Item '{name}' not found in the inventory. Cannot remove.")

# Example usage
inventory_manager = GroceryStoreInventory()

inventory_manager.add_item("Apple", 10, 165.75)
inventory_manager.add_item("Banana", 15, 70.75)
inventory_manager.view_inventory()

inventory_manager.update_item("Apple", 5, 55.75)
inventory_manager.view_inventory()

inventory_manager.remove_item("Banana")
inventory_manager.view_inventory()
