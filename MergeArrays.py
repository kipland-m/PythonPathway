# This program is a part of my program series that I will be using to nail Python as a whole.
# This program takes two given arrays and sorts them into a new array in an increasing order.

def ArraySorter(arr1,arr2):
    
    counter_1 = 0
    counter_2 = 0

    len1 = len(arr1)
    len2 = len(arr2)

    arr = []

    while((counter_1<len1) and (counter_2 < len2)):
        if(arr1[counter_1] < arr2[counter_2]):
            arr.append(arr1[counter_1])
            counter_1 += 1
        else:
            arr.append(arr2[counter_2])
            counter_2 += 1

    while(counter_1 < len1):
        arr.append(arr1[counter_1])
        counter_1 += 1

    while(counter_2 < len2):
        arr.append(arr2[counter_2])
        counter_2 += 1

    return arr

def UserInput():

    array1 = []
    array2 = []

    Active = True


    print("\nWelcome to Kipland's array sorter.")
    print("Please enter the numbers for your first array\n")

    counter = 0

    currentArray = 1

    while Active == True:

        print('Please enter "arr2" when you are ready to switch to array 2')
        print('Current amount of integers in array',currentArray,':',counter)

        arr_input = input('\n')
        print('\n')


        if arr_input != 'arr2':
            array1.append(int(arr_input))
                    
            counter += 1    
        


        if arr_input == 'arr2':

            currentArray = 2
            counter = 0

            while Active == True:

                print('Please type "quit" when you are ready to sort the two arrays.')
                print('Current amount of integers in array',currentArray,':',counter)

                arr_input = input('\n')
                print('\n')
                if arr_input != 'quit':
                    array2.append(int(arr_input))
                    counter += 1

                if arr_input == 'quit':
                    
                    Active = False
                    array1.sort()
                    array2.sort()
                    array = ArraySorter(array1,array2)
                    print(array)
                    




UserInput()

