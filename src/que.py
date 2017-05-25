"""Constructing the Stack data structure."""


from dll import DLinkedList


class Queue(object):
    """Define a stack and its methods."""

    def __init__(self):
        """Create a new empty queue."""
        self.newDLL = DLinkedList()

    def enqueue(self, val):
        """Add a new Node to the back of the queue."""
        return self.newDLL.push(val)

    def dequeue(self):
        """Remove the Node at the front of the queue."""
        return self.newDLL.shift()

    def peek(self):
        """Show the value of the next element in the queue."""
        return self.newDLL.tail.val

    def size(self):
        """Return the length of the queue."""
        return self.newDLL.length

    def __len__(self):
        """Return the length of the queue."""
        return self.newDLL.length
