# This program is a part of my program series that I will be using to nail Python as a whole.
# BubbleSorter.py contains an algorithm that "Bubble Sorts" a randomly generated array

import random

array_random = []

# This defines a function to fille array_random with 10 randoms numbers that can vary from 1-100
def ListFill(array):

    for i in range(10):
        array.append(random.randrange(1,101,1))

    return array

# Defines the sorter itself
def BubbleSorter(array):

    # This loop states that it will run the nested loop the length of given list -1, so if len(x_list) = 5 it will run nested loop 4 times.
    for i in range(0,len(array)-1):
        # This loop states it will run the same as above, only decreasing the amount of iterations based on the current iteration of the parent loop.
        # So, for example if the parent loop is on it's 6th iteration, it will subtract the amount of times the nested loop will run 6 times.
        for j in range(0,len(array)-1-i):
            # This if statement is a comparator to check the current number's value with the next number's value
            if (array[j] > array[j+1]):
                # If condition is met, this 'swapper' will switch the 2 number's values, 'sorting' them.
                array[j], array[j+1] = array[j+1], array[j]

    return array

print(BubbleSorter(ListFill(array_random)))





