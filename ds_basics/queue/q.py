

class Queue:

    def __init__(self) -> None:
        self.queue = []


    def enqueue(self, item):
        self.queue.append(item)


    def dequeue(self):
        if len(self.queue) < 1:
            return
        self.queue.pop(0)

    def __str__(self) -> str:
        return str(self.queue)

    def size(self):
        return len(self.queue)



q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q)

q.dequeue()

print("After removing an element")
print(q)
