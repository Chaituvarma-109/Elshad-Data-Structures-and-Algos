class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node

    def dequeue(self):
        if self.linkedList.head is None:
            return 'Queue is empty'
        else:
            return_value = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return return_value

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False

    def peek(self):
        if self.linkedList.head is None:
            return 'Queue is empty'
        return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
