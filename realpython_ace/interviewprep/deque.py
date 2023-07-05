"""
Deque is a doubly ended linked list
"""
from collections import deque

class TicketQueueDeque:
    """
    Ticket queue using a deque. A doubly ended linked list
    Part of the collections package
    """
    def __init__(self):
        self.deque = deque()


    def add_person(self, name):
        """
        Add to the back of the queue
        >>> queue = TicketQueue()
        >>> queue.add_person('Jack')
        Jack has been added to the queue.
        """
        self.deque.append(name)
        print(f"{name} has been added to the queue.")

    def service_person(self):
        """
        Service the end of the queue
        >>> queue = TicketQueue()
        >>> queue.add_person('Jack')
        Jack has been added to the queue.
        >>> queue.service_person()
        Jack has been serviced.
        """
        name = self.deque.popleft()
        print(f"{name} has been serviced.")

    def bypass_queue(self, name):
        """
        Bypass the queue entirely
        >>> queue = TicketQueue()
        >>> queue.add_person('Jack')
        Jack has been added to the queue.
        >>> queue.bypass_queue('Jill')
        Jill has bypassed the queue.
        >>> queue.service_person()
        Jack has been serviced.
        """
        self.deque.appendleft(name)
        print(f"{name} has bypassed the queue.")


class TicketQueue:
    """
    Ticket Queue using a list
    """

    def __init__(self):
        self.lst = list()

    def add_person(self, name):
        """
        Add to the back of the queue
        >>> queue = TicketQueue()
        >>> queue.add_person('Jack')
        Jack has been added to the queue.
        """
        self.lst.append(name)
        print(f"{name} has been added to the queue.")

    def service_person(self):
        """
        Service the end of the queue
        >>> queue = TicketQueue()
        >>> queue.add_person('Jack')
        Jack has been added to the queue.
        >>> queue.service_person()
        Jack has been serviced.
        """
        name = self.lst.pop()
        print(f"{name} has been serviced.")

    def bypass_queue(self, name):
        """
        Bypass the queue entirely
        >>> queue = TicketQueue()
        >>> queue.add_person('Jack')
        Jack has been added to the queue.
        >>> queue.bypass_queue('Jill')
        Jill has bypassed the queue.
        >>> queue.service_person()
        Jack has been serviced.
        """
        self.lst.insert(0, name)
        print(f"{name} has bypassed the queue.")
