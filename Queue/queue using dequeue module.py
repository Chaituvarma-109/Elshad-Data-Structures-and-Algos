import queue as q

custom_q = q.Queue(maxsize=3)
print(custom_q.qsize())

custom_q.put(10)
custom_q.put(20)
custom_q.put(30)
print(custom_q.qsize())

print(custom_q.empty())
print(custom_q.full())

print(custom_q.get())
print(custom_q.qsize())
