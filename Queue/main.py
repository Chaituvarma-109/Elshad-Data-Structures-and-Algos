class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(val) for val in self.list]
        return '\n'.join(values)

    def enqueue(self, val):
        self.list.append(val)

    def dequeue(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]

    def isEmpty(self):
        if self.list:
            return False
        return True

    def delete(self):
        self.list = None
        return self.list


cq = Queue()
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print(cq)
print('pop- ', cq.dequeue())
print('peek- ', cq.peek())
print(cq)
print(cq.delete())
