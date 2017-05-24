"""Constructing the Double Linked List data structure."""


class DNode(object):
    """."""

    def __init__(self, val, next, prev):
        """Create a new Node object with a val and a Node it points to."""
        self.val = val
        self.next = next
        self.prev = prev


class DLinkedList(object):
    """Define a linked list and its methods."""

    def __init__(self):
        """Create a new empty Linked List."""
        self.head = None
        self.length = 0

    def push(self, val):
        """Add a new Node to the head of the list."""
        new_next = self.head
        self.head = DNode(val, self.head, None)
        new_next.prev = self.head
        self.length += 1

    def pop(self):
        """Remove the head of the list and returns its value."""
        if self.head is not None:
            ret_val = self.head.val
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return ret_val
        else:
            raise IndexError('Linked list is empty')

    def remove(self, val):
        """Remove a given node from the list."""
        current_node = self.head
        val_exists = False
        if self.head.val == val:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            val_exists = True
        while current_node.next and not val_exists:
            if current_node.next.val == val:
                current_node.next.next.prev = current_node
                current_node.next = current_node.next.next
                self.length -= 1
                val_exists = True
                break
            current_node = current_node.next
        if not val_exists:
            raise IndexError('Node not in list')

    def __len__(self):
        """Return the length of the double list."""
        return self.length