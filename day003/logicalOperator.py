# 26. Logical Operators

# Roller Coaster Program; modified with if statement and now multiple if statment; now with
# logical operators for midlife crisis people

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
    elif 45 <= age <= 55:
        # dont need to set bill to 0 since after this it just skips everything
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")

    wantsPhoto = input("Do you want to have a photo taken? Type y for Yes and n for No: ")
    if wantsPhoto == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Your too short!  You cannot ride this rollercoaster!\n")
