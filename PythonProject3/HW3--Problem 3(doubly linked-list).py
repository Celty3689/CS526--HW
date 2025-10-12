class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def reverse_double_list(head):
    if head is None:
        return None

    if head.next is None:
        return head

    new_head = reverse_double_list(head.next)
    head.next.next = head
    head.prev = head.next
    head.next = None

    return new_head

#Create a doubly linked list
head = DoubleNode(1)
current = head

for i in range(2, 11):
    new_node = DoubleNode(i)
    current.next = new_node
    new_node.prev = current
    current = new_node

#Print the doubly linked-list
def print_double_list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

print("Input:", print_double_list(head))
new_head = reverse_double_list(head)
print("Output", print_double_list(new_head))