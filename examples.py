# voter_id = False

age = int(input("please enter your age: "))

if age >= 18:
    voter_id = input("do you have a voter id, yes or no:").lower()
    if voter_id == "yes":
        print("you are eligible")
    else:
        print("you meet the age requirment, please apply for voter id")
else: 
    print("you are not eligible")
