# athour: Anochili Blessing Ebele
# date: 29/09/2024
# purpuse : This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.



from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'."""
    # Get the current date and time
    current_date = datetime.now()

    # Format and print the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(days):
    """Calculates the date after adding the specified number of days to the current date."""
    # Get the current date and time
    current_date = display_current_datetime()

    # Add the specified number of days to the current date
    future_date = current_date + timedelta(days=days)

    # Format and print the future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    """Main function to run the script."""
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    try:
        # Prompt the user to enter the number of days
        days = int(input("Enter the number of days to add to the current date: "))
        
        # Calculate and display the future date
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
