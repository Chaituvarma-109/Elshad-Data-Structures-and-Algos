class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None


class DoublyLL:
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

    def create(self, val: int):
        new_node = Node(val)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node

    def insert(self, val: int, location: int):
        new_node = Node(val)
        if location == 0:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
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

    def traversal(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search(self, val):
        node = self.head
        while node:
            if node.data == val:
                print(f'{node.data} is present')
                break
            node = node.next
        else:
            print('List Does not exist')

    def delete(self, location):
        if self.head is None:
            print('Empty Linked List')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.deleteDLL()
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.deleteDLL()
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curr_node = self.head
                index = 0
                while index < location - 1:
                    curr_node = curr_node.next
                    index += 1
                curr_node.next = curr_node.next.next
                curr_node.next.prev = curr_node

    def deleteDLL(self):
        self.head = None
        self.tail = None


dsl = DoublyLL()
dsl.create(10)
dsl.insert(20, -1)
dsl.insert(15, 0)
dsl.insert(25, 2)
dsl.insert(30, 1)
print([n.data for n in dsl])
dsl.delete(0)
dsl.delete(-1)
dsl.delete(1)
print([n.data for n in dsl])
# dsl.traversal()
# dsl.deleteDLL()
