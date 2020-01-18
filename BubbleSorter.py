# This program is a part of my program series that I will be using to nail Python as a whole.
# BubbleSorter.py contains a recursive algorithm that "Bubble Sorts" a randomly generated array



import random

array_random = []

def ListFill(array):

    for i in range(10):
        array.append(random.randrange(1,101,1))

    return array


# This is the most broken program i have ever written. Need to be fixed.
def BubbleSorter(array):


    for i in range(0,len(array)-1):
        for j in range(0,len(array)-1-i):
            if (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]


    print(range(0,len(array)-1))
    return array


print(BubbleSorter(ListFill(array_random)))





