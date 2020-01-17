# This program is a part of my program series that I will be using to nail Python as a whole.

# Assuming given parameter is greater than or equal to 1 | Or just 0.
def Factorial(n):

    if (n >= 1):
        return n * Factorial(n-1)
    else:
        return 1


# Function Fibonacci will take "n" as parameter, in which said parameter returns value in corresponding
# position within Fibonacci sequence, so if n=4 it would return 4th number in Fibonacci sequence.
def Fibonacci(n):
    
    #If this condition is met it can be referred to as the recursive case
    if (n >= 3):
        return Fibonacci(n-1) + Fibonacci(n-2)

    #If this condition is met it can be referred to as the base case
    else:
        return 1

print(Factorial(3))
print(Fibonacci(4))