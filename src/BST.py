"""Implementing a Binary Search tree with In Order Traversal."""


class Node(object):
    def __init__(self, entry, left=None, iterable=None):
        """Node for tree."""
        self.val = entry
        self.left = left
        self.right = iterable


class BinarySearchTree(object):

    def __init__(self, iterable=None):
        # import pdb; pdb.set_trace()
        """This will sety what wwe will be iterating through."""
        self.visited = []
        self.list = []
        self.size = 0
        self.root = None
        if iterable:
            if type(iterable) in [list, tuple]:
                for element in iterable:
                    self.insert(element)

    def insert(self, entry):
        # import pdb; pdb.set_trace()
        if type(entry) not in [float, int]:
            raise TypeError("NUMBERS!!!!! numbers...")
        if not self.root:
            self.root = Node(entry)
            self.size += 1
        else:
            if entry > self.root.val:
                self.root.right = Node(entry)
            elif entry < self.root.val:
                self.root.left = Node(entry)
            else:
                curr = self.root
                while curr:
                    if entry > curr.val:
                        if curr.right:
                            previous = curr
                            curr = curr.right
                            continue
                        else:
                            curr.right = Node(entry)
                            self.size += 1
                    elif entry < curr.val:
                        if curr.left:
                            previous = curr
                            curr = curr.left
                            continue
                        else:
                            curr.left = Node(entry)
                            self.size += 1
                    else:
                        return

    def search(self, val):
        """."""
        if type(val) not in [float, int]:
            raise TypeError("SEARCH 4 NUMBERS!!!!! numbers...")
        if not self.root:
            return
        else:
            curr = self.root
            while curr:
                if val > curr.val:
                    if curr.right:
                        curr = curr.right
                        continue
                    else:
                        return
                elif val < curr.val:
                    if curr.left:
                        curr = curr.left
                        continue
                    else:
                        return
                else:
                    return curr

    def inOrderTrav(self, entry):
        # import pdb; pdb.set_trace()
        if entry is None:
            return
        self.inOrderTrav(entry.left)
        self.visited.append(entry.val)
        self.inOrderTrav(entry.right)

    def inOrder(self, root):
        # import pdb; pdb.set_trace()
        self.visited = []
        self.inOrderTrav(root)
        return self.visited
