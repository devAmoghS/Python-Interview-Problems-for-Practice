# The diameter of a tree (sometimes called the width) 
# is the number of nodes on the longest path between 
# two end nodes(leftmost leaf node and rightmost leaf node).

# The diameter of a tree T is the largest of the following quantities:
# the diameter of T’s left subtree
# the diameter of T’s right subtree
# the longest path between leaves that goes through the root of T (this can be computed from the heights of the subtrees of T)

# Algorithm:
# Case 1: if the diameter passes through origin, then diameter is
# height of left subtree + height of right subtree + 1 (root node)
# d = lheight + rheight + 1

# Case 2: if the diameter is not passing through origin
# Search for diameter in the left subtree and right subtree
# Pick the larger value of the two subtrees
# d = max(ldiameter, rdiameter)

# Finally take max of the two values since we do not 
# know if diameter is passing through the root or not
# d = max(lheight + rheight + 1, max(ldiameter, rdiameter))

class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def height(tree):
  if tree is None:
    return 0
  else:
    return 1 + max(height(tree.left), height(tree.right))

def diameter(tree):
  if tree is None:
    return 0

  else:
    lheight = height(tree.left)
    rheight = height(tree.right)

    ldiameter = diameter(tree.left)
    rdiameter = diameter(tree.right)

    return max(rheight + lheight + 1, max(ldiameter, rdiameter))

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print("Diameter of given binary tree is ",diameter(root))
