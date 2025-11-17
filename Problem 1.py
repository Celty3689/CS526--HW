import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def addNode(self, value):
        """Add a new node with given value to the BST"""
        if not self.root:
            self.root = Node(value)
            return
        curr = self.root
        while curr:
            if value < curr.value:
                if not curr.left:
                    curr.left = Node(value)
                    return
                curr = curr.left
            elif value > curr.value:
                if not curr.right:
                    curr.right = Node(value)
                    return
                curr = curr.right

    def deleteNode(self, value):
        """Delete node with given value from the BST"""
        def _delete(node, val):
            if not node:
                return None
            if val < node.value:
                node.left = _delete(node.left, val)
            elif val > node.value:
                node.right = _delete(node.right, val)
            else:
                # Node found - handle three cases
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # Node has two children - find inorder successor
                temp = node.right
                while temp.left:
                    temp = temp.left
                node.value = temp.value
                node.right = _delete(node.right, temp.value)
            return node

        self.root = _delete(self.root, value)

    def findNode(self, value):
        """Search for node with given value, return True if found"""
        curr = self.root
        while curr:
            if value == curr.value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def printTree(self):
        """Print BST using in-order traversal"""
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        result = []
        _inorder(self.root)
        print("BST:", result)

# Generate random input set of 5-50 numbers between 1-1000
input_set = random.sample(range(1, 1001), random.randint(5, 50))
print("Input Set:", input_set)

# Initialize BST with input set
bst = BST()
for num in input_set:
    bst.addNode(num)

print("Initial Tree:")
bst.printTree()

# Test AddNode operation
new_val = random.randint(1, 1000)
print(f"Adding {new_val}...")
bst.addNode(new_val)
bst.printTree()

# Test DeleteNode operation
del_val = random.choice(input_set)
print(f"Deleting {del_val}...")
bst.deleteNode(del_val)
bst.printTree()

# Test FindNode - positive case (should find existing value)
find_pos = random.choice(input_set)
print(f"Finding {find_pos}: {'Found' if bst.findNode(find_pos) else 'Not Found'}")

# Test FindNode - negative case (should not find non-existing value)
find_neg = random.randint(1, 1000)
while find_neg in input_set:
    find_neg = random.randint(1, 1000)
print(f"Finding {find_neg}: {'Found' if bst.findNode(find_neg) else 'Not Found'}")