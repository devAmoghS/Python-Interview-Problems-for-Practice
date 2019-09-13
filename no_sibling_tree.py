# Problem: Print the nodes of a binary tree
# which do not have a sibling


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printSingleNode(root, hasSibling):
    # hasSibling will check if root has both children
    if root is None:
        return
    else:
        # if root has one child, print that child data
        if not hasSibling:
            print("%d" % root.data)

        printSingleNode(root.left, root.right is not None)
        printSingleNode(root.right, root.left is not None)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.left.left = Node(6)

print("Level order traversal of binary tree is -")
printSingleNode(root, True)
