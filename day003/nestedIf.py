#24. Nested if statements and elseif

# Roller Coaster Program; modified with if statement

print("\nWelcome to the rollercoaster!")
height = int(input("What is your height in cm: "))

if height >= 120:
    print("You can ride this rollercoaster!")
    age = int(input("How old are you: "))
    if age <= 12:
        print("You only have to pay $5")
    elif age > 12 and age <= 18:
        print("You have to pay $7")
    else:
        print("You have to pay 12")
else:
    print("Your too short!  You cannot ride this rollercoaster!\n")
