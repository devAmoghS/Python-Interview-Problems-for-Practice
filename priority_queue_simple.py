# Priority Queue is an extension of the queue with following properties.
# 1) An element with high priority is dequeued before an element with low priority.
# 2) If two elements have the same priority, they are served according to their order in the queue
# The delete operation has time complexity of O(n)

class PriorityQueue(object):
  def __init__(self):
    self.queue = []
  
  def __str__(self):
    return ' '.join([str(i) for i in self.queue])

  # for checking if the queue is empty
  def isEmpty(self):
    return len(self.queue) == 0

  # for inserting an element in the queue
  def insert(self, data):
    self.queue.append(data)

  # for popping an element based on Priority
  def delete(self):
    try:
      max = 0
      
      for i in range(len(self.queue)):
        if self.queue[max] < self.queue[i]:
          max = i
        
      item = self.queue[max]
      del self.queue[max]
      
      return item

    except IndexError:
      print()
      sys.exit()

myQueue = PriorityQueue() 
myQueue.insert(12) 
myQueue.insert(1) 
myQueue.insert(14) 
myQueue.insert(7) 

print(myQueue)  

while not myQueue.isEmpty(): 
    print(myQueue.delete())
      
