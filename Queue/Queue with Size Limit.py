class Queue:
    def __init__(self, maxsize: int):
        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(val) for val in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.start == self.top + 1:
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def enqueue(self, value):
        if self.isFull():
            return "Queue is Full"
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            first_element = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxsize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items[self.start]

    def delete(self):
        self.items = self.maxsize * [None]
        self.start = -1
        self.top = -1


customQueue = Queue(3)
print(customQueue.isFull())
