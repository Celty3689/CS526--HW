def reverse_stack(stack):
    if len(stack) > 0:
        #Pop the top element from the stack.
        top = stack.pop()
        #Recursively reverse the remaining part.
        reverse_stack(stack)
        #Put the extracted element at the bottom.
        insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)

#test
stack = [1,2,3,4,5,6,7,8,9,10]
print("Input:", stack)
reverse_stack(stack)
print("Output:", stack)