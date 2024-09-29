# athour: Anochili Blessing Ebele
# date: 29/09/2024
# purpuse : Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.

def display_menu():
    """Displays the menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function that runs the shopping list manager."""
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt the user to add an item
            item = input("Enter the name of the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")

        elif choice == '2':
            # Prompt the user to remove an item
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':
            # Display the current shopping list
            if shopping_list:
                print("\nYour Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("\nYour shopping list is empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
