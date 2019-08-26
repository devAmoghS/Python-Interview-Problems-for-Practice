def findLowestCommonAncestor(root, value1, value2):
    while root is not None:
        value = root.value
        if value > value1 and value > value2:
            root = root.left
        elif value < value1 and value < value2:
            root = root.right
        else:
            return root
