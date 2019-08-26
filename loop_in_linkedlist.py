from linked_list_data_structure import LinkedList
from find_m_to_last_llist import findMToLast


def hasLoop(l_list):
    fast = l_list.head.next_node
    slow = l_list.head
    hasLoop = False

    while True:
        if fast or fast.next_node:
            pass
        elif fast == slow or fast.next_node == slow:
            hasLoop = True
        else:
            fast = fast.next_node
            slow = slow.next_node

    return hasLoop


linked_list = LinkedList()
# Returns the third element from last
print(findMToLast(linked_list))
