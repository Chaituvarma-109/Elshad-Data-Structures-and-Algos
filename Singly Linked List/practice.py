class Node:
    def __init__(self, val=None):
        self.data = val
        self.next = None


class SLL:
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
            print('List is empty')
        else:
            node = self.head
            while node is not None:
                print(node.data)
                node = node.next

    def search(self, val):
        if self.head is None:
            print('List is empty')
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.data == val:
                    return index + 1
                index += 1
                node = node.next
        return 'value not present'

    def delete(self, location):
        if self.head is None:
            print('list is empty')
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
                        node = node.next
                    node.next = None
                    self.tail = Node
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


sl1 = SLL()
# sl1.insert(55, 0)
# sl1.insert(245, -1)
# sl1.insert(900, 1)
# sl1.insert(10, 2)
# # sl1.traversal()
# print(sl1.search(10))
# print(sl1.search(0))
# sl1.delete_sll()
# print([node.data for node in sl1])
