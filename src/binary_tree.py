'''Constructing the Binary Tree Data Structure'''


class BiTree():

    def __init__(self, root):
        self.left = None
        self.right = None
        self.root = root

    def getLeftChi(self):
        return self.left

    def getRightChi(self):
        return self.right

    def setNodeVal(self, val):
        self.root = val

    def getNodeVal(self):
        return self.root

    def insRight(self, newNode):
        if self.right == None:
            self.right = BiTree(newNode)
        else:
            tree = BiTree(newNode)
            tree.right = self.right
            self.right = tree

    def insLeft(self, newNode):
        if self.left == None:
            self.left = BiTree(newNode)
        else:
            tree = BiTree(newNode)
            tree.left = self.left
            self.left = tree
