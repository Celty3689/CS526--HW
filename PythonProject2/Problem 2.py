#Problem 2: Create a linked list with 12,3,5,2

def doIt(node):
    #If the node is empty, return
    if node is None:
        return
    #Process the next node
    doIt(node[1])
    print(node[0])

node4 = [2, None]
node3 = [5, node4]
node2 = [3, node3]
node1 = [12, node2]

#Test function
doIt(node1)

"""Question: What would the doIt function produce with your list?
Answer: Reverse output: 2, 5, 3, 12"""