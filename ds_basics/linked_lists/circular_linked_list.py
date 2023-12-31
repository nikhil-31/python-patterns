
class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data


class CircularLinkedList:

    def __init__(self) -> None:
        self.head = None


    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head

        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next

            curr.next = new_node
            new_node.next = self.head
        


    def prepend(self, value):

        new_node = Node(value)
        curr = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        self.head = new_node


    def print_it(self):
        

        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break


cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_it()