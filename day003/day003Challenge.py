# Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = input('\tYou\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake_input = input('\tType "wait" to wait for a boat. Type "swim" to swim across\n').lower()
    if lake_input == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors")
        house_input = input("\tOne red, one yellow, one blue. Which color do you choose?\n").lower()
        if house_input == "yellow":
            print("You found the treasure! You Win!")
        elif house_input == "red":
            print("Burned by fire. Game Over")
        elif house_input == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("You chose a door that didn't exist. Game Over")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")