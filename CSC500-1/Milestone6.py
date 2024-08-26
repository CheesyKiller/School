# Author: Jacob Abts
# Submission Date: 8/18/2024
# CSU Global - CSC500-1

from datetime import date

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = ""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
        return total_cost
    
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")
        return self.item_description
    
    def getItemName(self):
        return self.item_name

class ShoppingCart:
    def __init__(self, customer_name = "None", date = date.today()):
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

    def remove_item(self, name):
        for i in range(0, len(self.items)):
            if (self.items[i].getItemName() == name):
                self.items.remove(self.items[i])
                return
        print("No item removed. Item not found!")

    def change_item_quantity(self, name):
        for item in self.items:
            if item.item_name == name:
                newQuantity = int(input("Enter new quantity: "))
                if newQuantity < 0:
                    newQuantity = 0
                item.item_quantity = newQuantity
                return
        print(f"\n{name} not found")

    def print_total(self):
        if len(self.items) != 0:
            print(f"{self.customer_name}'s Shopping Cart - {self.date}\nNumber of Items: {len(self.items)}\n")

            total_cost = 0

            for item in self.items:
                total_cost += item.print_item_cost()

            print(f"\nTotal: ${total_cost:.2f}")
        else:
            print("\nThere are no items in your cart.\n")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.date}\nItem Descriptions\n")

        for item in self.items:
            item.print_item_description()

def print_menu(customer_name):
    itemList = ShoppingCart()

    while (True):
        print("\nMain Menu\nA) Add an item to the cart\nR) Remove an item from the cart\nC) Change an item's quantity\nI) Output the list of item descriptions\nO) Output the shopping cart items\nQ) Quit\n")
        choice = str(input("Select an option: "))
        print()

        match choice:
            case "a" | "A":
                itemList.add_item()
            case "r" | "r":
                itemList.remove_item(str(input("Item to be removed: ")))
            case "c" | "C":
                itemList.change_item_quantity(str(input("Item to be changed: ")))
            case "i" | "I":
                itemList.print_descriptions()
            case "o" | "O":
                itemList.print_total()
            case "q" | "Q":
                return
            case _:
                print("\nPlease select a valid option.\n")

def main():
    print("Welcome to the shopping program!\n")
    print_menu(str(input("Enter your name: ")))

main()