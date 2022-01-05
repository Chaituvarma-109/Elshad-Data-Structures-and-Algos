class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None


class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next

    def create(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node

    def insert(self, val, location):
        new_node = Node(val)
        if location == 0:
            new_node.next = self.head
            new_node.prev = self.head.next
            self.head.prev = new_node.next
            self.head.next = self.tail
            self.head = new_node
        elif location == -1:
            new_node.next = None
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            curr_node = self.head
            index = 0
            while index < location - 1:
                curr_node = curr_node.next
                index += 1
            new_node.next = curr_node.next
            new_node.prev = curr_node
            curr_node.next.prev = new_node
            curr_node.next = new_node

    def delete(self):
        self.head = None
        self.tail = None


cdll = CircularDoublyLL()
cdll.create(10)
cdll.insert(20, 0)
cdll.insert(30, 0)
print([n.data for n in cdll])
