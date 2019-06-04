# This is a level order traversal of a 
# a binary tree. It is also known as breadth
# first traversal.

class Node:
  
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
def printLevelOrder(root):
  height = getHeight(root)
  if root is None:
    return
  else:
    # iteratively print all the levels
    for i in range(1, height+1):
      printGivenLevel(root, i)
      
def printGivenLevel(root, level):
  if root is None:
    return
  if level == 1:
    print("%d"%root.data)
  elif level > 1:
    # recursively print the given level
    printGivenLevel(root.left, level-1)
    printGivenLevel(root.right, level-1)

def getHeight(root):
  if root is None:
    return 0
  else:
    lheight = getHeight(root.left)
    rheight = getHeight(root.right)
    
    if(lheight > rheight):
      return lheight + 1
    else:
      return rheight + 1
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is -")
printLevelOrder(root)
