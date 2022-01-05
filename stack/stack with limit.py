class Stack:
    """
    Creating a Stack using Python List with size limit
    """
    def __init__(self, maxsize: int):
        self.maxsize = maxsize
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def push(self, val: int):
        if self.isFull():
            return 'Stack is Full'
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

    def isFull(self) -> bool:
        if len(self.list) == self.maxsize:
            return True
        return False

    def delete(self) -> None:
        self.list = None
