
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    
    
    def __init__(self) -> None:
        self.head = None


    def add_node(self, data):
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


linked_list = LinkedList()
linked_list.add_node(3)
linked_list.add_node(5)
linked_list.add_node(7)
