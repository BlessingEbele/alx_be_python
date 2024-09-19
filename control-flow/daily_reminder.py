#author: Blessing Ebele Anochili
#date: 18/09/2024
#purpose:This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks
    
# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
reminder_message = f"'{task}' is a "

match priority:
    case "high":
        reminder_message += "high priority task"
    case "medium":
         reminder_message += "medium priority task"
    case "low":
        reminder_message += "low priority task"
    case _:
        print("Invalid priority entered. Please choose high, medium, or low.")
        

    # Add time-bound message if necessary
if time_bound == "yes":
    reminder_message += " that requires urgent attention today!"
elif time_bound == "no":
    reminder_message += ". this task is no time bounded, you can complete it when you have free time."
else:
    print("Invalid input for time-bound. Please enter yes or no.")
    

 # Print the customized reminder
print(f"Reminder: {reminder_message}")