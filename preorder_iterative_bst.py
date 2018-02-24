def preOrderTraversal(root):
  stack = []
  stack.insert(0, root)
  while len(stack) > 0:
    current = stack.pop()
    print(current.value)
    
    right = current.right
    stack.insert(0, right) if right is not None
    
    left = current.left
    stack.insert(0, left) if left is not None
