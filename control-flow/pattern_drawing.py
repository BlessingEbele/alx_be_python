#author: Blessing Ebele Anochili
#date: 18/09/2024
#purpose: This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

size = int(input("Enter the size of the pattern:"))

#to ensure the user entered a positive number
if size <= 0:
    print("Please enter a positive interger")
    
rows = 0
while rows < size:
    #for loop to print *
    for _ in range(size +2):
        print("*", end="")
    print()
    rows += 1

        