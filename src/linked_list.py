"""Constructing the Linked List data structure."""


class Node(object):
    """."""

    def __init__(self, val, next):
        """."""
        self.val = val
        self.next = next


class LinkedList(object):
    """."""

    def __init__(self):
        """."""
        self.head = None
        self.length = 0

    def push(self, val):
        """."""
        self.head = Node(val, self.head)
        self.length += 1

    def pop(self):
        """."""
        if self.head is not None:
            ret_val = self.head.val
            self.head = self.head.next
            self.length -= 1
            return ret_val
        else:
            return 'Error: Linked List is empty'

    def size(self):
        """."""
        return self.length

    def __len__(self):
        """."""
        return self.length

    def __repr__(self):
        """."""
        current_node = self.head
        the_str = ''
        while current_node:
            the_str += '[{}] => '.format(current_node)
            current_node = current_node.next
        return the_str

    def remove(self, node):
        """."""
        current_node = self.head

        if self.head is node:
            self.head = self.head.next
        while current_node.next:
            if current_node.next is node:
                current_node.next = current_node.next.next
            current_node = current_node.next
