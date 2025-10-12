"""
Question 1:
What is the advantage of using a tail pointer in a linked list?

Answer:
The greatest advantage of using a tail pointer is that it enables the quick addition of new nodes at the end of the linked list.
Without a tail pointer, each time a node is added to the end of the list,
we need to traverse the entire list from the head to find the last node,
which is a rather time-consuming process.
With a tail pointer, the last node of the list can be accessed directly.
Using a tail pointer is good for situations where elements need to be frequently added at the end,
such as implementing a queue data structure.
In a queue, elements are always added at the tail and removed from the head.
The tail pointer makes the enqueue operation very fast.

"""