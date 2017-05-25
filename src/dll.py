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
        """Create a new empty Doubly Linked List."""
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        """Add a new DNode to the head of the list."""
        new_next = self.head
        self.head = DNode(val, self.head, None)
        if self.head.next is None:
            self.tail = self.head
        else:
            new_next.prev = self.head
        self.length += 1

    def append(self, val):
        """Add a new DNode to the tail of the list."""
        new_prev = self.tail
        self.tail = DNode(val, None, self.tail)
        if self.tail.prev is None:
            self.head = self.tail
        else:
            new_prev.next = self.tail
        self.length += 1

    def pop(self):
        """Remove the head of the list and returns its value."""
        if self.head is not None:
            ret_val = self.head.val
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return ret_val
        else:
            raise IndexError('Linked list is empty')

    def shift(self):
        """Remove the tail of the list and returns its value."""
        if self.tail is not None:
            ret_val = self.tail.val
            if self.tail.prev is not None:
                self.tail.prev.next = None
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            self.length -= 1
            return ret_val
        else:
            raise IndexError('Linked list is empty')

    def remove(self, val):
        """Remove a given node from the list based on its val."""
        current_node = self.head
        val_exists = False
        if self.head.val == val:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            val_exists = True
        if self.tail.val == val:
            self.tail = self.tail.prev
            self.tail.next = None
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
