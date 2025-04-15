# 25. Multiple if statement in succession

#24. Nested if statements and elseif

# Roller Coaster Program; modified with if statement and now multiple if statment

print("\nWelcome to the rollercoaster!")
height = int(input("What is your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride this rollercoaster!")
    age = int(input("How old are you: "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age > 12 and age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    wantsPhoto = input("Do you want to have a photo taken? Type y for Yes and n for No: ")
    if wantsPhoto == "y":
        bill += 3
    print(f"Your final bill is $ {bill}")
else:
    print("Your too short!  You cannot ride this rollercoaster!\n")
