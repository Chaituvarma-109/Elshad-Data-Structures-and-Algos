class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, val, location):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if temp_node == self.tail:
                    self.tail = new_node

    def traversal(self):
        if self.head is None:
            print('Head is present')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search(self, val):
        if self.head is None:
            print('Head is present')
        else:
            node = self.head
            while node is not None:
                if node.value == val:
                    return node.value
                node = node.next
            return 'value does not exist'

    def delete(self, location):
        if self.head is None:
            print('SLL is empty')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next

    def delete_sll(self):
        self.head = self.tail = None


sll1 = SinglyLinkedList()
sll1.insert(23, 1)
sll1.insert(22, 0)
sll1.insert(55, 2)
sll1.insert(33, 1)
sll1.insert(100, -1)
sll1.insert(200, 3)
print([node.value for node in sll1])
# sll1.traversal()
# print(sll1.search(10))
# print(sll1.search(100))
sll1.delete(4)
sll1.delete_sll()
print([node.value for node in sll1])
