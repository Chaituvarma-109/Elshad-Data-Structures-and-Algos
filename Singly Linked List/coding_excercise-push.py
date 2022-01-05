class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def get(self, ind):
        if ind < 0 or ind >= self.length:
            return None
        curr_node = self.head
        index = 0
        while curr_node:
            if index == ind:
                return curr_node
            index += 1
            curr_node = curr_node.next

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        self.length += 1
        print('Success')

    def insert(self, index, val):
        if index < 0 or index >= self.length - 1:
            return False
        else:
            curr_node = self.head
            for ind in range(index-1):
                curr_node = curr_node.next
            next_node = Node(val)
            next_node.next = curr_node.next
            curr_node.next = next_node
            self.length += 1
        return True

    def pop(self):
        if self.length == 1:
            remove_node = self.head
            self.head = self.tail = None
            self.length -= 1
            return remove_node
        elif self.length > 1:
            node = self.head
            while node is not None:
                if node.next == self.tail:
                    remove_node = node.next
                    break
                node = node.next
            node.next = None
            self.tail = node
            self.length -= 1
            return remove_node
        else:
            return 'Undefined'


sl1 = SinglyLinkedList()
sl1.push(5)
# print(sl1.length)
# print(sl1.head.val)
# print(sl1.tail.val)

sl1.push(10)
# print(sl1.length)
# print(sl1.head.val)
# print(sl1.head.next.val)
# print(sl1.tail.val)

sl1.push(15)
sl1.push(20)

print(sl1.insert(2, 12))
print(sl1.insert(4, 25))
print(sl1.insert(1, 30))
print([node.val for node in sl1])

# print(sl1.get(3).val)
# print(sl1.get(1).val)
# print(sl1.get(0).val)
# print(sl1.get(4).val)
# print(sl1.get(5).val)

# print('pop', sl1.pop().val)
# print('tail-', sl1.tail.val)
# print('1', sl1.length)
# print('1', [node.val for node in sl1])
# print('pop', sl1.pop().val)
# print('2', [node.val for node in sl1])
# print('2', sl1.length)
# print('pop', sl1.pop())
