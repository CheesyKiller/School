# Author: Jacob Abts
# Submission Date: 9/8/2024
# CSU Global - CSC500-1

from datetime import date

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = ""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def get_item_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
        return total_cost
    
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")
        return self.item_description
    
    def get_item_name(self):
        return self.item_name

class ShoppingCart:
    def __init__(self, customer_name = "None", date = "January 1, 2020"):
        self.customer_name = customer_name
        if (type(date) == str):
            self.date = date
        else:
            self.date = f"{months[date.month]} {date.day}, {date.year}"
        self.items = []
    
    def add_item(self):
        print(f"Item {len(self.items) + 1}")

        item_name = str(input("Enter the item name: "))
        item_price = round(float(input("Enter the item price: ")), 2)
        item_quantity = int(input("Enter the item quantity: "))
        item_description = str(input("Enter the item description: "))

        self.items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    def remove_item(self):
        name = str(input("Item to be removed: "))
        for i in range(0, len(self.items)):
            if (self.items[i].get_item_name() == name):
                self.items.remove(self.items[i])
                return
        print("No item removed. Item not found!")

    def change_item_quantity(self, name):
        for item in self.items:
            if item.item_name == name:
                newQuantity = int(input("\nEnter new quantity: "))
                if newQuantity < 0:
                    newQuantity = 0
                    self.remove_item(name)
                item.item_quantity = newQuantity
                return
        print(f"\n{name} not found")

    def change_item_price(self, name):
        for item in self.items:
            if item.item_name == name:
                newPrice = float(input("\nEnter new price: "))
                if newPrice < 0:
                    newPrice = 0
                item.item_price = newPrice
                return
        print(f"\n{name} not found")

    def change_item_description(self, name):
        for item in self.items:
            if item.item_name == name:
                newDescription = str(input("\nEnter new description: "))
                item.item_description = newDescription
                return
        print(f"\n{name} not found")

    def modify_item(self):
        if len(self.items) < 1:
            print("There are no items in your cart!")
            return
        
        itemToModify = str(input("Enter an item to modify: "))

        for item in self.items:
            if itemToModify == item.get_item_name():
                while (True):
                    performAction = str(input("\nWhat would you like to do?\nA) Change item quantity\nB) Change item price\nC) Change item description\nQ) Quit to main maneu\n\n"))
                    match performAction:
                        case "a" | "A":
                            self.change_item_quantity(itemToModify)
                        case "b" | "B":
                            self.change_item_price(itemToModify)
                        case "c" | "C":
                            self.change_item_description(itemToModify)
                        case "q" | "Q":
                            return
                        case _:
                            print("\nPlease select a valid option.")
        print(f"\n{itemToModify} not found")

    def get_num_items_in_cart(self):
        return len(self.items)

    def get_cost_of_cart(self):
        total_cost = 0

        for item in self.items:
            total_cost += item.get_item_cost()
        return total_cost

    def print_total(self):
        if len(self.items) != 0:
            print(f"{self.customer_name}'s Shopping Cart - {self.date}\nNumber of Items: {len(self.items)}\n")

            total_cost = 0

            for item in self.items:
                total_cost += item.print_item_cost()

            print(f"\nTotal: ${total_cost:.2f}")
        else:
            print("There are no items in your cart.")

    def print_descriptions(self):
        if len(self.items) != 0:
            print(f"{self.customer_name}'s Shopping Cart - {self.date}\nItem Descriptions\n")

            for item in self.items:
                item.print_item_description()
        else:
            print("There are no items in your cart.")

def print_menu(customer_name):
    itemList = ShoppingCart(customer_name, date.today())

    while (True):
        print("\nMain Menu\nA) Add an item to the cart\nR) Remove an item from the cart\nM) Modify an item\nI) Output the list of item descriptions\nO) Output the shopping cart items\nQ) Quit\n")
        choice = str(input("Select an option: "))
        print()

        match choice:
            case "a" | "A":
                itemList.add_item()
            case "r" | "r":
                itemList.remove_item()
            case "m" | "M":
                itemList.modify_item()
            case "i" | "I":
                itemList.print_descriptions()
            case "o" | "O":
                itemList.print_total()
            case "q" | "Q":
                return
            case _:
                print("Please select a valid option.")

def main():
    print("Welcome to the shopping program!\n")
    print_menu(str(input("Enter your name: ")))

main()