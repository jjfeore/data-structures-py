"""Constructing the Linked List data structure."""


class Node(object):
    """Define the Node object."""

    def __init__(self, val, next):
        """Create a new Node object with a val and a Node it points to."""
        self.val = val
        self.next = next


class LinkedList(object):
    """Define a linked list and its methods."""

    def __init__(self, iterable=None):
        """Create a new empty Linked List."""
        if type(iterable) in [list, tuple, str]:
            self.head = None
            self.length = 0
            for val in iterable:
                self.push(val)
        else:
            self.head = None
            self.length = 0

    def push(self, val):
        """Add a new Node to the head of the list."""
        self.head = Node(val, self.head)
        self.length += 1

    def pop(self):
        """Remove the head of the list and returns its value."""
        if self.head is not None:
            ret_val = self.head.val
            self.head = self.head.next
            self.length -= 1
            return ret_val
        else:
            raise IndexError('Linked list is empty')

    def size(self):
        """Return the length of the list."""
        return self.length

    def display(self):
        """Return a string with all the list Node values and their order."""
        current_node = self.head
        the_str = '('
        if not current_node:
            the_str += ')'
        while current_node:
            the_str += str(current_node.val)
            if current_node.next is None:
                the_str += ')'
            else:
                the_str += ', '
            current_node = current_node.next
        return the_str

    def __len__(self):
        """Return the length of the list."""
        return self.length

    def __repr__(self):
        """Return what the display method returns."""
        return self.display()

    def remove(self, node):
        """Remove a given node from the list."""
        current_node = self.head
        node_exists = False
        if not current_node or not node:
            raise IndexError('Node not in list')
        if self.head is node:
            self.head = self.head.next
            self.length -= 1
            node_exists = True
        while current_node.next and not node_exists:
            if current_node.next is node:
                current_node.next = current_node.next.next
                self.length -= 1
                node_exists = True
                break
            current_node = current_node.next
        if not node_exists:
            raise IndexError('Node not in list')

    def search(self, val):
        """Return the first Node containing the value."""
        curr = self.head

        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return None
