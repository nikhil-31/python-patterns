

class Queue:

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.size > 0:
            return self.queue.pop(0)

    def __str__(self) -> str:
        return str(self.queue)

    def size(self):
        return len(self.queue)
    
    def __len__(self):
        return self.size



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
