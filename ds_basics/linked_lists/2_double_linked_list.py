class Node:

    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedList():

    def __init__(self):
        self.head = None

    
    def insert_into_empty_list(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("List is not empty")



    def insert_to_the_end(self, data):
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    

    def delete_at_start(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        self.head = self.head.next
    
    
    def delete_at_end(self):

        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
    
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None


    def display(self):
        if self.head is None:
            print("The list is empty")

        else:
            temp = self.head
            while temp is not None:
                data = temp.data
                print("The data is: ", data)
                temp = temp.next 

        print("\n")

NewDoublyLinkedList = DoublyLinkedList()
# Insert the element to empty list
NewDoublyLinkedList.insert_into_empty_list(10)
# Insert the element at the end
NewDoublyLinkedList.insert_to_the_end(20)
NewDoublyLinkedList.insert_to_the_end(30)
NewDoublyLinkedList.insert_to_the_end(40)
NewDoublyLinkedList.insert_to_the_end(50)
NewDoublyLinkedList.insert_to_the_end(60)
# Display Data
NewDoublyLinkedList.display()
# Delete elements from start
NewDoublyLinkedList.delete_at_start()
# Delete elements from end
NewDoublyLinkedList.delete_at_end()
# Display Data
NewDoublyLinkedList.display()

