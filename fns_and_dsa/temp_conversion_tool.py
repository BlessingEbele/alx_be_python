# athour: Anochili Blessing Ebele
# date: 29/09/2024
# purpose: . This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

# fns_and_dsa/temp_conversion_tool.py

# Global conversion factors (checked for definition)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Ensure this is defined correctly

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function to run the temperature conversion tool
def main():
    """Main function to handle user input and temperature conversion."""
    try:
        # Prompt user for temperature input
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    # Prompt user for the temperature unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Perform the appropriate conversion
    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Run the main function
if __name__ == "__main__":
    main()
