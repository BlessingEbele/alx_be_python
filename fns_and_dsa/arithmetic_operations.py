# athour: Anochili Blessing Ebele
# date: 23/09/2024
# purpuse : In this script, define a function that performs basic arithmetic operations. This function, perform_operation, will be imported and used in a separate main.py script, which we provide.
# arithmetic_operations.py


def perform_operation(num1, num2, operation):
    # Perform the arithmetic operation based on the input
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"
