"""
Binary tree

"""

class Node:
    """
    This is a node class to create a b-tree
    To create an object pass a key
    """

    def __init__(self, key) -> None:
        self.right = None
        self.left = None
        self.key = key

''' 
following is the tree after above statement
        1
      /   \
     None  None
'''
# CREATING THE ROOT

root = Node(1)

'''
2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
None None None None
'''
root.left = Node(2)
root.right = Node (3)
