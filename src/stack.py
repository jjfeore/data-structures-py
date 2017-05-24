"""Constructing the Stack data structure."""


from linked_list import Node


class Stack(object):
    """Define a stack and its methods."""

    def __init__(self, iterable=None):
        """Create a new empty stack."""
        if type(iterable) in [list, tuple, str]:
            self.head = None
            self.length = 0
            for val in iterable:
                self.push(val)
        else:
            self.head = None
            self.length = 0

    def push(self, val):
        """Add a new Node to the head of the stack."""
        self.head = Node(val, self.head)
        self.length += 1

    def pop(self):
        """Remove the head of the stack and returns its value."""
        if self.head is not None:
            ret_val = self.head.val
            self.head = self.head.next
            self.length -= 1
            return ret_val
        else:
            raise IndexError('Stack is empty')

    def __len__(self):
        """Return the length of the stack."""
        return self.length
