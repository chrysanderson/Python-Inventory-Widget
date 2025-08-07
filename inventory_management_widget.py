#---Drone Inventory Management---

#import time module to work with time within the program
import time

#dictionary of inventory items and quantity
inventory = {
    "repair kits": 5,
    "energy cells": 10,
    "plasma cutters": 2,
}

#variable to change in order to stop loop
running = True

#main loop to keep program running
while running:

#menu
    print("\n Main Menu")
    print("-" * 30)
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update")
    print("5. Quit")

    choice = input("Please select '1 - 4' \n: ")
    time.sleep(1)

#view inventory
    if choice == '1':
        print("\n---Current Inventory---")

        for item, quantity in inventory.items():
            print(f"{item.title()}: {quantity}")

        time.sleep(2)

#add item to inventory
    elif choice == '2':
        print("\n ---Add New Item---")
        item_name = input("enter name of new item. \n: ").lower()

        try:
            quantity = int(input(f"please enter the quantity of {item_name.title()}.\n:  "))

            inventory[item_name] = quantity

            print(f"Added {quantity} of {item_name} to the Inventory")
            time.sleep(1)
        except ValueError:
            print("invalid input, please enter a number.")
        
        time.sleep(1)

#remove item from inventory
    elif choice == '3':
        print("\n ---Remove Item---")

        item_name = input("Please enter name of item you would like to remove.\n: ").lower()

        try:
            inventory.pop(item_name)

            print(f"{item_name} removed from inventory")

        except KeyError:
            print(f"{item_name} not in inventory.")

        time.sleep(1)

#update quantity of item within inventory
    elif choice == '4':
        print("\n ---Update Item---")

        item_name = input("please enter the name of the item you wish to update the quantity of.\n: ").lower()
        
        if item_name in inventory:
            try:
                quantity = int(input(f"please enter the new quantity for {item_name}.\n: "))
        
                inventory[item_name] = quantity

                print(f"The new quantity of {item_name} is {quantity}.")

            except ValueError:
                print(f"invalid input, please enter a number")
        
        else:
            print(f"{item_name} not in inventory.")

        time.sleep(1)

#close program
    elif choice == '5':

        running = False
        
#if user enters something other than a valid option
    else:
        print("please enter a number '1 - 5'.")
        time.sleep(1)