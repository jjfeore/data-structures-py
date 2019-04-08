"""Implementing a Binary Search tree with In Order Traversal."""


class Node(object):
    def __init__(self, entry, left=None, iterable=None, parent=None):
        """Node for tree."""
        self.val = entry
        self.left = left
        self.right = iterable
        self.parent = parent


class BinarySearchTree(object):

    def __init__(self, iterable=None):
        # import pdb; pdb.set_trace()
        """This will sety what wwe will be iterating through."""
        self.visited = []
        self.list = []
        self.size = 0
        self.root = None
        self.iterable = iterable
        if iterable is not None:
            if type(iterable) in [list, tuple]:
                for element in iterable:
                    self.list.append(element)
                    self.insert(element)

    def insert(self, entry):
        # import pdb; pdb.set_trace()
        if type(entry) not in [float, int]:
            raise TypeError("NUMBERS!!!!! numbers...")
        if not self.root:
            self.root = Node(entry)
            self.size += 1
        else:
            curr = self.root
            while curr:
                if entry > curr.val:
                    if curr.right:
                        curr = curr.right
                        continue
                    else:
                        curr.right = Node(entry)
                        self.size += 1
                        curr.right.parent = curr
                        self.balance_manager(curr)
                elif entry < curr.val:
                    if curr.left:
                        curr = curr.left
                        continue
                    else:
                        curr.left = Node(entry)
                        self.size += 1
                        self.balance_manager(curr)
                        curr.left.parent = curr
                else:
                    return

    def search(self, entry):
        """."""
        if type(entry) not in [float, int]:
            raise TypeError("NUMBERS!!!!! numbers...")
        else:
            curr = self.root
            while curr:
                if entry > curr.val:
                    if curr.right:
                        curr = curr.right
                        continue
                elif entry < curr.val:
                    if curr.left:
                        curr = curr.left
                        continue
                else:
                    return curr

    def depth_first(self, entry):
        if entry is None:
            return 0
        left_depth = self.depth_first(entry.left)
        right_depth = self.depth_first(entry.right)
        if (left_depth > right_depth):
            return left_depth + 1
        return right_depth + 1

    def breadth_first(self):
        self.nodes_to_visit = []
        curr = self.root
        self.nodes_to_visit.append(curr)
        while self.nodes_to_visit:
            curr = self.nodes_to_visit.pop(0)
            if curr.left:
                self.nodes_to_visit.append(curr.left)
            if curr.right:
                self.nodes_to_visit.append(curr.right)
            yield curr

    def pre_order_trav(self, entry=None):
        if entry:
            curr = entry
        else:
            curr = self.root
        yield curr.val
        if curr.left:
            for item in self.pre_order_trav(curr.left):
                yield item
        if curr.right:
            for item in self.pre_order_trav(curr.right):
                yield item

    def pre_order(self):
        for node_data in self.pre_order_trav():
            yield node_data

    def in_order_trav(self, entry=None):
        if entry:
            curr = entry
        else:
            curr = self.root
        if curr.left:
            for item in self.in_order_trav(curr.left):
                yield item
        yield curr.val
        if curr.right:
            for item in self.in_order_trav(curr.right):
                yield item

    def in_order(self):
        for node_data in self.in_order_trav():
            yield node_data

    def post_order_trav(self, entry=None):
        if entry:
            curr = entry
        else:
            curr = self.root
        if curr.left:
            for item in self.post_order_trav(curr.left):
                yield item
        if curr.right:
            for item in self.post_order_trav(curr.right):
                yield item
        yield curr.val

    def post_order(self):
        for node_data in self.post_order_trav():
            yield node_data

    def check_that_balance(self, target=None):
        """check the balance of your treeeee"""
        if self.size == 0:
            return 0
        if target is not None:
            return self.depth_first(target.right) - self.depth_first(target.left)

    def find_min_depth(self, target):
        if target.left is None:
            return target
        if target.left is not None:
            target = target.left
            return target

    def find_max_depth(self, target):
        if target.right is None:
            return target
        if target.right is not None:
            target = target.right
            return target

    def deletion(self, target):
        """nope"""
        delete_node = self.search(target)
        if delete_node is None:
            return 'This is the end!'
        else:
            self.size -= 1
            if delete_node.left is None and delete_node.right is None:
                if delete_node.val > delete_node.parent.val:
                    delete_node.parent.right = None
                else:
                    delete_node.parent.left = None
            elif delete_node.left and not delete_node.right:
                if delete_node.val > delete_node.parent.val:
                    delete_node.parent.right = delete_node.left
                    delete_node.left.parent = delete_node.parent
                else:
                    delete_node.parent.left = delete_node.left
                    delete_node.left.parent = delete_node.parent
            elif delete_node.right and not delete_node.left:
                if delete_node.val > delete_node.parent.val:
                    delete_node.parent.right = delete_node.right
                    delete_node.right.parent = delete_node.parent
                else:
                    delete_node.parent.left = delete_node.right
                    delete_node.left.parent = delete_node.parent
            else:
                if self.check_that_balance(target) > 0:
                    min_val = self.find_min_depth(delete_node.right)
                    delete_node.val = min_val.val
                    if min_val.right is None:
                        min_val.parent.left = None
                        min_val.parent = None
                    else:
                        min_val.val = min_val.right.val
                        min_val.right.parent = None
                        min_val.right = None
                else:
                    max_val = self.find_max_depth(delete_node.left)
                    delete_node.val = max_val.val
                    if max_val.left is None:
                        max_val.parent.right = None
                        max_val.parent = None
                    else:
                        max_val.val = max_val.left.val
                        max_val.left.parent = None
                        max_val.left = None

    def balance_manager(self, node=None):
        # import pdb; pdb.set_trace()
        if node is None:
            node = self.root
        if self.size % 2 == 0:
            if self.check_that_balance(node) > 1:
                self.rotate_right()
            if self.check_that_balance(node) < -1:
                self.rotate_left()
        else:
            if self.check_that_balance(node) > 0:
                self.rotate_right()
            if self.check_that_balance(node) < 0:
                self.rotate_left()

    def rotate_left(self, node=None):
        if node is None:
            node = self.root
        origin = node
        node = self.find_max_depth(origin.left)
        if node.val > node.parent.val:
            if node.parent.parent is None:
                node.right = origin
                node.right.parent = node
                node.right.left = None
                node.parent = None
                node = self.root
                return
            node.left = node.parent.parent
            node.parent = node.left.parent
            node.right = node.left.right
            node.right.parent = node
            node.left.parent = node.left
            node.parent.right = node
        else:
            node.right = origin
            node.left = origin.left
            origin.left = None
            origin = node
            origin.parent.right = None
            origin.parent = None

    def rotate_right(self, node=None):
        # import pdb; pdb.set_trace()
        if node is None:
            node = self.root
        origin = node
        node = self.find_min_depth(origin.right)
        if node.val > node.parent.val:
            if node.parent.parent is None:
                node.left = origin
                node.left.parent = node
                node.left.right = None
                node.parent = None
                node = self.root
                return
            node.right = node.parent.parent
            node.parent = node.right.parent
            node.left = node.right.left
            node.left.parent = node
            node.right.parent = node.right
            node.parent.left = node
        else:
            node.left = origin
            node.right = origin.right
            origin.right = None
            origin = node
            origin.parent.left = None
            origin.parent = None

    # def balance_that_thang(self, node=None):
    #     # import pdb; pdb.set_trace()
    #     if not node:
    #         node = self.root
    #     gen = self.breadth_first()
    #     for i in [i for i in gen]:
    #         self.balance_manager(i)


if __name__ == '__main__':  # pragma: no cover
    b = BinarySearchTree([5, 3, 7, 2, 8, 4, 9, 1])
    gen = b.in_order()
    [i for i in gen]
