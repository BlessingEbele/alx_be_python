# athour: Anochili Blessing Ebele
# date: 29/09/2024
# purpuse : This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.



# fns_and_dsa/temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Correct definition added here

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    """Main function to interact with the user and perform temperature conversions."""
    try:
        # Ask the user for the temperature and conversion type
        temp = float(input("Enter the temperature value: "))
        conversion_type = input("Choose conversion type (F to C / C to F): ").strip().upper()

        # Perform the conversion based on user's input
        if conversion_type == "F TO C":
            result = fahrenheit_to_celsius(temp)
            print(f"{temp} Fahrenheit is {result:.2f} Celsius.")
        elif conversion_type == "C TO F":
            result = celsius_to_fahrenheit(temp)
            print(f"{temp} Celsius is {result:.2f} Fahrenheit.")
        else:
            print("Invalid conversion type. Please choose 'F to C' or 'C to F'.")

    except ValueError:
        print("Invalid input. Please enter a valid numeric temperature.")

if __name__ == "__main__":
    main()
