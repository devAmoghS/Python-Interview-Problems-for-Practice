# Problem: Find the no. of nodes in a BST that lies in a given range

# Algorithm: We will traverse the tree recursively until we encounter leaf nodes (Base case)
# else we do the following
# 1. Current node is less than the given range --> Traverse the right subtree
# 2. Current node is more than the given range --> Traverse the left subtree
# 3. Current node lies in the given range      --> Increment Count; Traverse both the left and right subtree

# Data Structure for Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def nodesWithinRange(root, range):
    low, high = range
    # this is the base case
    if root is None:
        return 0
    # optional: to improve efficiency
    elif root.data == high or root.data == low:
        return 1
    # if the current node lies in the range
    elif root.data <= high and root.data >= low:
        return (
            1 + nodesWithinRange(root.left, range) + nodesWithinRange(root.right, range)
        )
    # if the current node lies in left subtree
    elif root.data > high:
        return nodesWithinRange(root.left, range)
    # if the current node lies in the right subtree
    elif root.data < low:
        return nodesWithinRange(root.right, range)

if __name__ == "main":
    
    node = Node(10)
    node.left = Node(5)
    node.left.left = Node(1)
    node.right = Node(50)
    node.right.left = Node(45)
    node.right.right = Node(100)

    result = nodesWithinRange(node, (5, 45))
    print(result)
