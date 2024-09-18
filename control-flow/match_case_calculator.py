#author: Blessing Ebele Anochili
#date: 18/09/2024
#purpose: This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). The script will then perform the selected operation using a Match Case statement and display the result.

#collecting input from user
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):.")

match operation:
    case "+":
        result = num1 + num2
        print("The result is", result)
    case "-":
        result = num1 - num2
        print("The result is", result)
    case "*":
        result = num1 * num2
        print("The result is", result)
    case "/":
        if num2 != 0:
            result = num1 / num2
            print("The result is", result)
        else:
            print("Cannot divide by zero.")
    case _:
	    print("Invalid operation selected. please choose one of +, -, *, or /.")