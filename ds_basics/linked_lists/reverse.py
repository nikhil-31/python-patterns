"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    
    def __init__(self) -> None:
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while ( current is not None):
            next = current.next 
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def push(self, new_data):
        """
        Inserting at the beginning
        """
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next


# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print ("Given linked list")
llist.print_list()
llist.reverse()
print ("\nReversed linked list")
llist.print_list()