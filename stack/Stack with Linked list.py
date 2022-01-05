class Node:
    def __init__(self, value: int = None):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    """
    Creating Stack using Linked List
    """
    def __init__(self):
        self.linkedlist = LinkedList()

    def push(self, val: int):
        new_node = Node(val)
        new_node.next = self.linkedlist.head
        self.linkedlist.head = new_node

    def pop(self):
        if not self.linkedlist.head:
            return 'Stack is empty'
        else:
            temp_node = self.linkedlist.head
            self.linkedlist.head = self.linkedlist.head.next
            return temp_node.data

    def peek(self):
        if not self.linkedlist.head:
            return 'Stack is empty'
        else:
            return self.linkedlist.head.data

    def isEmpty(self):
        if self.linkedlist.head:
            return False
        return True

    def delete(self):
        self.linkedlist.head = None


sll = Stack()
sll.push(0)
sll.push(5)
sll.push(10)
print(sll.pop())
print(sll.peek())
print(sll.isEmpty())
sll.delete()
print(sll.linkedlist.head)
