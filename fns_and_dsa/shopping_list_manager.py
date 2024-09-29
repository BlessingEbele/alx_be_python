# athour: Anochili Blessing Ebele
# date: 29/09/2024
# purpuse : Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.

# shopping_list_manager.py

def display_menu():
    """Displays the menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function that runs the shopping list manager."""
    
    # Check that the shopping list is implemented as a list (array)
    shopping_list = []
    if not isinstance(shopping_list, list):
        raise TypeError("shopping_list must be a list")

    while True:
        # Check if display_menu function exists and is callable
        if not callable(display_menu):
            raise NameError("display_menu function is not defined or callable")
        
        # Call display_menu function
        display_menu()

        # Ensure choice input is a number (integer)
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        # Handle the user's choice
        if choice == 1:
            # Prompt the user to add an item
            item = input("Enter the name of the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")

        elif choice == 2:
            # Prompt the user to remove an item
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == 3:
            # Display the current shopping list
            if shopping_list:
                print("\nYour Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("\nYour shopping list is empty.")

        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
