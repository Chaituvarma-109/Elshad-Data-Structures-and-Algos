class Stack:
    """
    Creating a Stack using Python List without size limit
    """
    def __init__(self):
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def push(self, val: int) -> None:
        self.list.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.list.pop()
        return 'stack is empty'

    def peek(self):
        if not self.isEmpty():
            return self.list[len(self.list) - 1]
        return 'stack is empty'

    def isEmpty(self) -> bool:
        if self.list:
            return False
        return True

    def delete(self) -> None:
        self.list = None


cstack = Stack()
cstack.push(10)
cstack.push(20)
cstack.push(30)
print(cstack.peek())
print(cstack.pop())
print(cstack.isEmpty())
cstack.delete()
print(cstack)
