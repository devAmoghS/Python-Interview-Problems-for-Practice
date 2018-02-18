class Node:
  def __init__(self, data=None):
    self.data = data
    self.next_node = None
    
  def getData(self):
    return self.data
    
  def setData(self, data):
    self.data = data
    
  def getNextNode(self):
    return self.next_node
    
  def setNextNode(self, new_next):
    self.next_node = new_next
    
class LinkedList:
  def __init__(self, head=None):
    self.head = head
    
  def isEmpty(self):
    return self.head == None
    
  def insert(self, data):
    temp = Node(data)
    temp.setNextNode(self.head)
    self.head = temp
    
  def size(self):
    current = self.head
    count = 0
    while current:
      count+=1
      current.getNextNode()
    return count
    
  def search(self, data):
    current = self.head
    found = False
    while current and not found:
      if current.getData() == data:
        found = True
      else:
        current = current.getNextNode()
    if current is None:
      raise ValueError("Data is not in the list")
    return current
    
    def delete(self, data):
      current = self.head
      previous = None
      found = False
      while current and not found:
        if current.getData() == data:
          found = True
        else:
          previous = current
          current = current.getNextNode()
      if current is None:
        raise ValueError("Data is not in the list")
      if previous is None:
        self.head = current.getNextNode()
      else:
        previous.setNextNode(current.getNextNode())
          
