# This program is a part of my program series that I will be using to nail Python as a whole.
# Inside LinkedList.py is a demonstration of a linked list that contains a function to update
# and count how many nodes are in a linked list



class Node:
    
    data = 0

    def __init__(self,data):
        super().__init__()

        self.data = data
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        super().__init__()
        self.head = None

if __name__ == "__main__":

    #Creating an empty linked list
    linkedList = LinkedList()

    #Assigns the first partition in the linked list (or "head") to attribute passed through Node()
    linkedList.head = Node(12)

    #Following partitions in linked list are created below
    second = Node(25)
    third = Node(55)
    fourth = Node(56)

    #Below is the code to link partitions within linked list together
    linkedList.head.next = second
    second.next = third
    third.next = fourth

    #Below is code to link partitions to previous node in linked list
    second.prev = linkedList.head
    third.prev = second
    fourth.prev = third


    # Function countForwards counts from the head node in linked list and returns value equal to total
    # partitions inside linked list
    def countForwards(head):
        count = 1
        current = linkedList.head

        while(current.next != None):
            current = current.next
            count += 1

        return count

    # Function countBackwards counts from the last node in linked list and returns value equal to total
    # partitions inside linked list
    def countBackwards(Node):
        count = 1
        current = fourth

        while(current.prev != None):
            current = current.prev
            count += 1

        return count


    print(countBackwards(fourth))
    print(countForwards(linkedList.head))



