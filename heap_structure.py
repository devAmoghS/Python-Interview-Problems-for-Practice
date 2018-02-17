class Heap(object):
  
  HEAP_SIZE = 10;
  
  def __init__(self):
    self.heap = [0]*Heap.HEAP_SIZE
    self.currentPosition = -1
    
  def insert(self, item):
    
    # if heap is full , we print a notification
    if self.isFull():
      print("Heap is full")
      return
    # else, increment the currentPosition and add item
    self.currentPosition+=1
    self.heap[self.currentPosition] = item
    self.fixUp(self.currentPosition)
    
  def fixUp(self, index):
    parentIndex = int((index-1)/2)
    while parentIndex >=0 and self.heap[parentIndex] < self.heap[index]:
      # if True swap heap[index] and heap[parentIndex]
      temp = self.heap[index]
      self.heap[index] = self.heap[parentIndex]
      self.heap[parentIndex] = temp
      # update the index and parentIndex
      index = parentIndex
      parentIndex = int((index-1)/2)
  
  def fixDown(self, index, upto):
    if upto < 0:
      upto = self.currentPosition
      
    while index<=upto:
      leftChild = 2*index+1
      rightChild = 2*index+2
      
      if leftChild <= upto:
        childToSwap = 0
      else:
        if self.heap[leftChild] < self.heap[rightChild]:
          childToSwap = leftChild
        else:
          childToSwap = rightChild
      
      if self.heap[index] < self.heap[childToSwap]:
        temp = self.heap[index]
        self.heap[index] = self.heap[childToSwap]
        self.heap[childToSwap] = temp
      else:
        break
      
      index = childToSwap
      
    else:
      return
    
  def heapSort(self):
    for i in range(0, self.currentPosition+1):
      temp = self.heap[0]
      print("%d"%temp)
      self.heap[0] = self.heap[self.currentPosition-i]
      self.heap[self.currentPosition-i] = temp
      self.fixDown(0, self.currentPosition-i-1)
      
  def getMax():
    result = self.heap[0]
    self.currentPosition-=1
    self.heap[0] = self.heap[self.currentPosition]
    del self.heap[self.currentPosition]
    self.fixDown(0, -1)
    return result
    
  def isFull(self):
    return self.currentPosition == Heap.HEAP_SIZE
    
some_heap=Heap()
some_heap.insert(12)
some_heap.insert(-3)
some_heap.insert(21)
some_heap.insert(7)
some_heap.insert(4)
some_heap.heapSort()
