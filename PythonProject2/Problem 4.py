#Problem 4: Write a function to find the sum of the three middle nodes in a doubly linked list of sorted integers.

def sum_middle_three(head):
    #Calculate the number of nodes in a linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    middle_pos = length//2

    current = head
    for i in range(middle_pos):
        current = current.next

    return current.prev.value + current.value + current.next.value

#Create a doubly linked list
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

#Create nodes and connect them
n1 = Node(2)
n2 = Node(4)
n3 = Node(8)
n4 = Node(10)
n5 = Node(15)
n6 = Node(29)
n7 = Node(41)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4
n5.next = n6
n6.prev = n5
n6.next = n7
n7.prev = n6

print(sum_middle_three(n1))