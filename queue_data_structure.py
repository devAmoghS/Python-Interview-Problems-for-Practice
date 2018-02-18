class Queue:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, value):
    self.queue.insert(0, value)
    
  def dequeue(self):
    self.queue.pop()
    
  def isEmpty(self):
    return self.size() == 0
    
  def size(self):
    return len(self.queue)
