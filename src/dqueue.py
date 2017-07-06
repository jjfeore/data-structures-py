"""Implement a double ended queue."""


from dll import DLinkedList


class Dque(object):
    """Define dqueue and its methods."""

    def __init__(self):
        """Create a new empty dqueue."""
        self.new_dll = DLinkedList()

    def append(self, val):
        """Add a new value to the end of the queue."""
        self.new_dll.append(val)

    def appendleft(self, val):
        """Add a new value to the start of the queue."""
        self.new_dll.push(val)

    def pop(self):
        """Remove the value that is at the end of the queue."""
        return self.new_dll.shift()

    def popleft(self):
        """Remove the value at the front of the queue."""
        return self.new_dll.pop()

    def peek(self):
        """Return the value that is at the end of the queue."""
        if self.new_dll.tail:
            return self.new_dll.tail.val
        return None

    def peekleft(self):
        """Return the value that is at the front of the queue."""
        if self.new_dll.head:
            return self.new_dll.head.val
        return None

    def size(self):
        """Return the size of the queue."""
        return self.new_dll.length
