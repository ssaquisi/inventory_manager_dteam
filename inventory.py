class Product:
    def __init__(self, name, quantity=0, price=0.0, category="General"):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} (Qty: {self.quantity}, Price: ${self.price:.2f}, Category: {self.category})"

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, quantity=0, price=0.0, category="General"):
        self.inventory[name] = Product(name, quantity, price, category)

    def list_products(self):
        if not self.inventory:
            return "Inventory is empty"

        output = "Products:\n"
        for product in self.inventory.values():
            output += f"- {product}\n"
        return output.strip()

    def update_quantity(self, name, quantity):
        if name in self.inventory:
            self.inventory[name].quantity = quantity
            return True
        return False

    def remove_product(self, name):
        if name in self.inventory:
            del self.inventory[name]
            return f"Product {name} was removed"
        return f"Product {name} was not found"


def main():
    manager = InventoryManager()

    while True:
        print("\n===== Inventory Manager =====")
        print("1. Add product")
        print("2. List products")
        print("3. Update quantity")
        print("4. Remove product")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            name = input("Product name: ")
            try:
                quantity_input = input("Quantity (default 0): ")
                quantity = int(quantity_input) if quantity_input else 0
                
                price_input = input("Price (default 0.0): ")
                price = float(price_input) if price_input else 0.0
            except ValueError:
                print("Invalid number format. Product not added.")
                continue
            
            category = input("Category (default General): ") or "General"
            
            manager.add_product(name, quantity, price, category)
            print("Product added successfully.")

        elif option == "2":
            print(manager.list_products())

        elif option == "3":
            name = input("Product name: ")
            try:
                quantity = int(input("New quantity: "))
            except ValueError:
                print("Invalid quantity format.")
                continue

            if manager.update_quantity(name, quantity):
                print("Quantity updated.")
            else:
                print("Product not found.")

        elif option == "4":
            name = input("Product name: ")
            print(manager.remove_product(name))

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()