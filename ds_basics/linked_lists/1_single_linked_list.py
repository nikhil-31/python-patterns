
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    
    
    def __init__(self) -> None:
        self.head = None


    def detect_cycle(self):

        fast = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


    def get_middle(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


    def delete_middle(self):

        if self.head.next is None:
            return None
        
        slow = self.head
        fast = self.head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return self.head



    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next 
        return prev


    def reverse_recursive(self):

        def _reverse(curr, prev):

            if not curr:
                return prev
            
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            return _reverse(curr, prev)
        prev = _reverse(self.head, None)

        return prev


    def add_node(self, data):
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        # Add at the end
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    def print_list(self):

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node


    def delete_node(self, key):
        
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None


    def len(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count
    
    
    def len_recursive(self, node):
        if node is None:
            return 0    
        else:
            return 1 + self.len_recursive(node)
        

    def find_duplicates(self):

        duplicates = dict()
        prev = None
        curr = self.head

        while curr:
            if curr in duplicates:
                curr.next = prev.next
                curr = None
            else:
                duplicates[curr.data] = 1
                prev = curr
            curr = prev.next


    def count_occurances(self, data):

        count = 0
        curr = self.head
        while curr:
            if curr.data == data:
                count +=  1
        return count

    def count_recursively(self, node, data):

        if node is None:
            return 0
        elif node.data == data:
            return 1 + self.count_recursively(node.next, data)
        else:
            return self.count_recursively(node.next, data)
        

    def move_to_last(self):

        if self.head and self.head.next:
            last = self.head
            second_to_last = None

            while last.next:
                second_to_last = last
                last = last.next
            
            last.next = self.head
            second_to_last.next = None
            self.head = last


    def merge_sorted(self, llist):

        p = self.head
        q = llist.head

        s = None

        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head
    
    
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return

        current = self.head
        new_node = Node(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
    
        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1



linked_list = LinkedList()
linked_list.add_node(3)
linked_list.add_node(5)
linked_list.add_node(7)


print(f"Detecting cycle {linked_list.detect_cycle()}")
print(f"Middle {linked_list.get_middle().data}")

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

print("Linked list 1")
llist_1.print_list()

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

print("Linked list 2")
llist_2.print_list()

llist_1.merge_sorted(llist_2)
print("Merged list")
llist_1.print_list()
