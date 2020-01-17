# This program is a part of my program series that I will be using to nail Python as a whole.
# The purpose of GCD_Calculator is to take the user's input and calculater the greatest common divisor.


# Function EuclideanGCD solves the GCD by determining the larger of the two numbers given and utilizing the Modulus operator
# Example: x = 72 y = 55 the code would determine that x is the higher of the two numbers and modulus x by y
# All whilst checking that neither numbers are equal to zero
def EuclideanGCD(x,y):

    x = abs(x)
    y = abs(y)

    if x == 0 and y == 0:
        return None

    if x == 0 and not y == 0:
        return y

    if not x == 0 and y == 0:
        return x

    if x > y:
        return Main(x % y,y)

    else:
        return Main(y % x,x)


print(EuclideanGCD(21,22))
