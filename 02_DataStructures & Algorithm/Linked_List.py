class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# first = Node(1)
# second = Node(2)
# third = Node(3)
# fourth = Node(4)
# first.next = second
# second.next = third
# third.next = fourth

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else: 
            ptr = self.head
            while(ptr.next):
                ptr = ptr.next
            ptr.next = new_node
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    

# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.insert(idx = 2, value = 9)