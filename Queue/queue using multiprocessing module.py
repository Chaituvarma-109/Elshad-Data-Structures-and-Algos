from multiprocessing import Queue

custom_q = Queue(maxsize=3)

custom_q.put(10)
print(custom_q.get())
