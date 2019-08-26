class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def isEmpty(self):
        return self.head == None

    def insert(self, data):
        # create a temp node
        temp = Node(data=data)
        # point new node to head
        temp.next_node = self.head
        # set the head as new node
        self.head = temp

    def insert_after(self, prev, data):
        if prev is None:
            raise ValueError("Given node is not found...")
            return prev

        # create a temp node
        temp = Node(data=data)
        # set next node of temp to the next node of previous
        temp.next_node = prev.next_node
        # set next node of previous to point temp
        prev.next_node = temp

    def size(self):
        # start with the head
        current = self.head
        count = 0

        # loop unless current is not None
        while current:
            count += 1
            current = current.next_node
        return count

    def search(self, data):
        # start with the head
        current = self.head
        found = False

        # loop unless current is not None
        while current and not found:
            # if found, change flag and return data
            if current.data == data:
                found = True
            else:
                # change current to next node
                current = current.next_node
        if current is None:
            # raise Exception if not found
            raise ValueError("Data is not in the list")
        return current

        def delete(self, data):
            # start with the head
            current = self.head
            previous = None
            found = False

            # loop unless current is not None
            while current and not found:
                # if found, change flag
                if current.getData() == data:
                    found = True
                else:
                    previous = current
                    current = current.next_node

            if current is None:
                # raise Exception if not found
                raise ValueError("Data is not in the list")
            if previous is None:
                self.head = current.next_node
            else:
                previous.next_node = current.next_node
