

class Deque:

    def __init__(self) -> None:
        self.items = []

    
    def size(self):
        return len(self.items)


    def is_empty(self):
        return self.size() == 0

    
    def addFront(self, item):
        self.items.insert(0, item)


    def addRear(self, item):
        self.items.append(item)


    def removeFront(self):
        if not self.is_empty():
            self.items.pop(0)


    def removeRear(self):
        if not self.is_empty():
            self.items.pop()

d = Deque()
print(d.is_empty())
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
print(d.size())
print(d.is_empty())
d.addRear(11)
print(d.removeRear())
print(d.removeFront())
d.addFront(55)
d.addRear(45)
print(d.items)