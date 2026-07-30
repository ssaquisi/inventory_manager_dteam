class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity=0):
        self.inventory[product] = quantity

    def list_products(self):
        if not self.inventory:
            return "Inventory is empty"

        output = "Products:\n"
        for product, quantity in self.inventory.items():
            output += f"- {product}: {quantity}\n"
        return output.strip()

    def update_quantity(self, product, quantity):
        if product in self.inventory:
            self.inventory[product] = quantity
            return True
        return False

    def remove_product(self, product):
        if product in self.inventory:
            del self.inventory[product]
            return f"Product {product} was removed"
        return f"Product {product} was not found"


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
            product = input("Product name: ")
            quantity = int(input("Quantity: "))
            manager.add_product(product, quantity)
            print("Product added successfully.")

        elif option == "2":
            print(manager.list_products())

        elif option == "3":
            product = input("Product name: ")
            quantity = int(input("New quantity: "))

            if manager.update_quantity(product, quantity):
                print("Quantity updated.")
            else:
                print("Product not found.")

        elif option == "4":
            product = input("Product name: ")
            print(manager.remove_product(product))

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()