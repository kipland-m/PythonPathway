# This program is a part of my program series that I will be using to nail Python as a whole.
# The purpose of ReverseString.py is to take a user's input and output their string reversed.

def Main(data):

    data = data[::-1]
    print("Your reversed string: "+data)

def UserInput():

    print("Please input the string you would like to be reversed.")
    user_string = input("Choice: ")
    Main(user_string)

UserInput()


