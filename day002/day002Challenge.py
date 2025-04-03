# Day 2 Project: Tip Calculator
print(f"Welcome to the tip calculator!")

# calculations

# ask the user for the bill and converts to float for math later
bill = float(input("What was the total bill? $"))
# asks the user for how much tip they would like to tip
tipPercentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
# converts the tip number, ex: 12, to a percentage by diving by 100; ex: 12/100 = .12
tipPercentage = tipPercentage/100
# asks the user how many people are going to split the bill
peopleToSplit = int(input("How many people to split the bill? "))
# calculate the total bill split, total bill, then how much the tip was
totalBill = bill*(1+tipPercentage)
totalBillSplit = totalBill/peopleToSplit
tipAmount = bill*tipPercentage

# output
print(f"\nEach person should pay: ${(round(totalBillSplit, 2))}")
print(f"The tip amount was: ${round(tipAmount, 2)}")
print(f"The total bill with tip is: ${round(totalBill, 2)}")