class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next

    def __len__(self):
        return self.length

    def create(self, val):
        node = Node(val)
        node.next = node
        self.head = node
        self.tail = node
        self.length += 1

    def insert(self, val, location):
        new_node = Node(val)
        if location == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        elif location == -1:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for ind in range(location - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        if self.head is None:
            print('empty')
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
            if node == self.tail.next:
                break

    def search(self, val):
        if self.head is None:
            print('empty')
        node = self.head
        while node:
            if node.data == val:
                print(f'{node.data} is present')
                break
            node = node.next
            if node == self.tail.next:
                break

    def singleNode(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        self.length -= 1

    def deleteCSSL(self, location):
        if self.head is None:
            return 'Empty'
        else:
            if location == 0:
                if self.length == 1:
                    self.singleNode()
                elif self.length > 1:
                    self.head = self.head.next
                    self.tail.next = self.head
                    self.length -= 1
            elif location == -1:
                if self.length == 1:
                    self.singleNode()
                elif self.length > 1:
                    curr_node = self.head
                    while curr_node:
                        if curr_node.next == self.tail:
                            break
                        curr_node = curr_node.next
                    curr_node.next = self.head
                    self.tail = curr_node
                    self.length -= 1
            else:
                curr_node = self.head
                index = 0
                while index < location - 1:
                    curr_node = curr_node.next
                    index += 1
                next_node = curr_node.next
                curr_node.next = next_node.next
                self.length -= 1

    def entireCSSL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


csl1 = CircularSLL()
csl1.create(1)
csl1.insert(0, 0)
csl1.insert(2, -1)
csl1.insert(3, -1)
csl1.insert(25, 2)
print([n.data for n in csl1])
csl1.deleteCSSL(0)
csl1.deleteCSSL(-1)
csl1.deleteCSSL(2)
print([n.data for n in csl1])
print(csl1.head.data)
print(csl1.tail.next.data)
print(len(csl1))
