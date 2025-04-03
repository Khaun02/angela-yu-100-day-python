# 17. Number Manipulation and F Strings in Python

bmi = 84/ 1.65**2
# not really clean way to output since so many numbers after
    #print(int(bmi))

# by using int() we "floor" the number, gets to the nearest whole number and removes all decimal places
# we want to "round" the number

    #print(round(bmi))

# instead of just simply rounding, we can add another parameter to round to the ndigits
print(round(bmi, 2))

# assignment operator
# accumulate results of our calculations
# += -= *= and /=
score = 0
score+=1
print(f"old score: {score}")

# f strings
    #print(f""")

# easy to combine different datatypes, cuts a lot of work to convert other data types to str
score+=2
print(f"new score: {score}")