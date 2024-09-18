#author: Blessing Ebele Anochili
#date: 18/09/2024
#purpose:  This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.

number = float(input("Enter a number to see its multiplication table:"))

for i in range (1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")