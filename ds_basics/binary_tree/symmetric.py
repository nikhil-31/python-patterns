from .queue import Queue


def symmetric(node):

    if node is None:
        return False

    queue = Queue()

    queue.enqueue(node.left)
    queue.enqueue(node.right)

    while queue:
        left = queue.dequeue()
        right = queue.enqueue()
        
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.data != right.data:
            return False
        
        queue.enqueue(left.left)
        queue.enqueue(right.right)
        queue.enqueue(left.right)
        queue.enqueue(right.left)

    return True
