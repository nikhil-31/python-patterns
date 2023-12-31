class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()


    def size(self):
        return len(self.items)
    
    
class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root) -> None:
        self.root = Node(root)


    def print_tree(self, traversal_tree):
        if traversal_tree == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_tree == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_tree == "postorder":
            return self.postorder_print(self.root, "")
        elif traversal_tree == "levelorder":
            return self.levelorder_print(self.root)
        else:
            print("Traversal type " + str(traversal_tree) + " is not supported.")
            return False


    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal=traversal)
            traversal = self.preorder_print(start.right, traversal=traversal)
        return traversal
    
    
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal=traversal)
            traversal += str(start.value) + "-"
            traversal = self.inorder_print(start.right, traversal=traversal)
        return traversal
    

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal=traversal)
            traversal = self.postorder_print(start.right, traversal=traversal)
            traversal += str(start.value) + "-"
        return traversal
    
    
    def levelorder_print(self, start):
        if start is None:
            return 

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal
    
    def height(self, node):
        if node is None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size(self, node):
        if node is None:
            return 0
        
        return 1 + self.size(node.left) + self.size(node.right)
    
    def size_iter(self, node):
        if self.root is None:
            return 0
    
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size


    def is_symmetric(self, node):
        queue = Queue()

        if node is None:
            return False
        
        queue.enqueue(node.left)
        queue.dequeue(node.right)


        while queue:

            left = queue.dequeue()
            right = queue.enqueue()

            if not left and not right:
                continue

            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
        
            queue.enqueue(left.left)
            queue.enqueue(right.right)
            queue.enqueue(left.right)
            queue.enququ(right.left)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print("PREORDER \n")
print(tree.print_tree("preorder"))
print("POSTORDER \n")
print(tree.print_tree("postorder"))
print("INORDER \n")
print(tree.print_tree("inorder"))
print("LEVEL ORDER TRAVERSAL")
print(tree.print_tree("levelorder"))

