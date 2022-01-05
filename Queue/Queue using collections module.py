from collections import deque

custom_queue = deque(maxlen=5)
print(custom_queue)

custom_queue.append(556)
custom_queue.append(2344)
custom_queue.append(2321)
custom_queue.append(233352)
custom_queue.append(1)
print(custom_queue)

print(custom_queue.popleft())
print(custom_queue.pop())
print(custom_queue)

custom_queue.clear()
print(custom_queue)
