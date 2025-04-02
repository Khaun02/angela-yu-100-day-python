# 15. Type Error, Checking and Conversion

# Q: how to know data type of "Hello"
    #print(type("Hello"))
    #print(type(123))
    #print(type(3.141592653))
    #print(type(True))

    #print(int("123") + int("456"))

# make this line run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))

# my answer
    # print("Number of letters in your name: " + str(len(input("Enter your name"))))

# angela way
user_name = input("Enter your name")
name_length = str(len(user_name))
print("Number of letters in your name: " + name_length)
