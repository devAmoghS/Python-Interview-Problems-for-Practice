# Given a linked list, this method
# will return m'th element to the last
# 2->3->4->8->5; m=2 will return 8
# since 8 is second to last

def findMToLast(l_list, m):
  current = l_list.head
  count = 0
  
  while current is not None and count < m:
    count+=1
    current = current.getNextNode()
  
  m_behind = l_list.head
  while current.next_node is not None:
    current = current.getNextNode()
    m_behind = m_behind.getNextNode()
    
  return m_behind
  
linked_list = LinkedList()
m_to_last = 3
# Returns the third element from last
print(findMToLast(linked_list, m_to_last))
