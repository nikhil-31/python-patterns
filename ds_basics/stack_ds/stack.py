

class Stack:

    def __init__(self):
        self.stack = []


    def check_empty(self):
        return len(self.stack) == 0


    def push(self, item):
        self.stack.append(item)


    def pop(self):
        if self.check_empty():
            return
        self.stack.pop()


    def __str__(self) -> str:
        return str(self.stack)


stack = Stack()

stack.push(8)
stack.push("1")
stack.push("p")
stack.push(1)

stack.pop()
stack.pop()
stack.pop()
stack.pop()

print("Elements in the stack: " + str(stack))
