class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    #An empty linked list or a linked list with only one node
    if head is None or head.next is None:
        return head
    #Recursively reverse the remaining part.
    new_head = reverse_list(head.next)
    #Append the current node to the end of the reversed list.
    head.next.next = head
    head.next = None

    return new_head

#Create the linked-list:
head = Node(1)
current = head
for i in range(2, 11):
    current.next = Node(i)
    current = current.next

#Print the linked-list
def print_list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

print("Input:", print_list(head))
new_head = reverse_list(head)
print("Output:", print_list(new_head))