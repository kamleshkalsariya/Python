from collections import deque
import time
import threading

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

orders = ['pizza','samosa','pasta','biryani','burger']
q = Queue()
def take_order(orders):
    for item in orders:
        q.enqueue(item)
        time.sleep(0.5)
        print (q.buffer)

def serve_order(q):
    for i in range(q.size()):
        print(q.dequeue())
        time.sleep(2)


t1 = threading.Thread(target=take_order, args=(orders,))
t2 = threading.Thread(target=serve_order, args=(q,))

t1.start()
time.sleep(2)
t2.start()