# Given a binary tree, find the second largest
# node in it

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def find_largest(root):
    current = root
    while current is not None:
        if current.right is not None:
            return current.right.data
        current = current.right

def find_second_largest(root):
    if root is None or (root.left is None and root.right is None):
        raise ValueError("Tree must atleast have 2 nodes")
        
    current = root
    
    while current is not None:
        if(current.left is not None and current.right is None):
            return find_largest(current.left)
        
        if(current.right is not None and current.right.left is None and current.right.right is None):
            return current.data
            
        current = current.right
    
node = Node(10)
node.left = Node(5)
node.left.left = Node(1)
node.right = Node(50)
node.right.left = Node(45)
node.right.right = Node(100)

result = find_second_largest(node)
print(result) # prints 50
