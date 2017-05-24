"""Constructing the Stack data structure."""


from linked_list import LinkedList


class Stack(object):
    """Define a stack and its methods."""

    def __init__(self, iterable=None):
        """Create a new empty stack."""
        self.newlinkedlist = LinkedList(iterable)

    def push(self, val):
        """Add a new Node to the head of the stack."""
        return self.newlinkedlist.push(val)

    def pop(self):
        """Remove the head of the stack and returns its value."""
        return self.newlinkedlist.pop()

    def __len__(self):
        """Return the length of the stack."""
        return self.newlinkedlist.size()
