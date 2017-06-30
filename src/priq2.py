class Node(object):
    """Define the Node object."""

    def __init__(self, val, next):
        """Create a new Node object with a val and a Node it points to."""
        self.val = val
        self.next = next


class Priq2(object):
    """Define a linked que and its methods."""

    def __init__(self, iterable=None):
        """Create a new empty Linked que."""
        self.pist = []
        if type(iterable) in [list, tuple, str]:
            raise TypeError('plz insert an integer')
        elif type(iterable) in [list, tuple, str]:
            self.parent = None
            self.length = 0
            for val in iterable:
                self.insert(val)
        else:
            self.parent = None
            self.length = 0

    def insert(self, val, pri=0):
        """Add a new Node to the parent of the Que."""
        self.parent = Node(val, self.parent)
        self.length += 1
        new_item = [pri, val]
        if new_item[0] is None and self.pist:
            new_item[0] = self.pist[-1][0]
        self.pist.append(new_item)

    def pop(self):
        """Remove the parent of the que and returns its value."""
        if self.parent is not None:
            ret_val = self.parent.val
            self.parent = self.parent.next
            self.length -= 1
            return ret_val
        else:
            raise IndexError('PriQ is empty')

    def size(self):
        """Return the length of the que."""
        return self.length

    def display(self):
        """Return a string with all the que Node values and their order."""
        current_node = self.parent
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
        """Return the length of the que."""
        return self.length

    def __repr__(self):
        """Return what the display method returns."""
        return self.display()