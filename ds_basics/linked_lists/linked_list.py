
class Node:
    
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, value):
        new_node = Node(value)
        temp = self.head
        new_node.next = temp
        self.head = new_node


    def insert_at_end(self, value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node


    def insert_after(self, prev_node, new_value):
        if prev_node is None:
            print("Node does not exist")
            return
        
        new_node = Node(new_value)
        temp = prev_node.next
        new_node.next = temp
        prev_node.next = new_node


    def delete_node(self, position):
        
        if self.head is None:
            return

        if position == 0:
            self.head = self.head.next

        temp = self.head
        for i in range(position - 1):
            if temp.next is None:
                return
            temp = temp.next

        if temp is None:
            return

        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next


    def reverse(self):
        prev = None
        current = self.head
        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
    

    def search(self, key):
        current = self.head

        while current is not None:
            if current.item == key:
                return True
            current = current.next
        return False

    def print(self):
        temp = self.head
        while (temp != None):
            data = temp.item
            print(data)
            temp = temp.next

    def middle(self):
        
        slow = self.head
        fast = self.head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        middle = slow.item
        return middle


llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_beginning(2)
llist.insert_at_beginning(3)
llist.insert_at_end(4)
llist.insert_after(llist.head.next, 5)

print('linked list:')
llist.print()

print("\nAfter deleting an element:")
llist.delete_node(3)
llist.print()

print()
item_to_find = 3
if llist.search(item_to_find):
    print(str(item_to_find) + " is found")
else:
    print(str(item_to_find) + " is not found")



