class Node:
  def __init__(self, value=None, children=[]):
    self.value = value
    self.children = children
    
  def getValue(self):
    return self.value
    
  def setValue(self, new_value):
    self.value = new_value
    
  def getNumChildren(self):
    return len(self.children)
    
  def getChild(self, index):
    return self.children[index]
    
root = Node(5,[Node(2), Node(6)])
print(root.getValue()) # 5
print(root.getNumChildren()) # 2
print(root.getChild(1)) # <Node object at 0x7f856fe764e0>
