# This program is a part of my program series that I will be using to nail Python as a whole.

# 2D Array, an array that contains other arrays
# Each element inside array_2d can be called as an element, so array_2d[1] = [22,31,45,89,91]
array_2d = [[1,3,66,11],[22,31,45,89,91],[67,11,2]]

# This function finds the sum of all numbers contained in each nested array
def TwoDimensionalArray(array):

    total = 0

    # This practically states for each array in array do this:
    for row in array:
        # This states for each element in each nested array do this:
        for i in row:
            
            total += i

    return total

print(TwoDimensionalArray(array_2d))