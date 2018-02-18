class Stack:
  def __init__(self):
    self.stack = []
    
  def push(self, value):
    self.stack.append(value)
    
  def pop(self):
    if self.isEmpty():
      print("Stack underflow...")
      return None
    else:
      self.stack.pop()
    
  def size(self):
    return len(self.stack)
    
  def isEmpty(self):
    return self.size() == 0
    
  def peek(self):
    if self.isEmpty():
      return None
    else:
      return self.stack[-1]
